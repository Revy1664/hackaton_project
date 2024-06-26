from django.shortcuts import render, redirect

from .forms import QuestionAnswerForm, SubjectForm
from .models import QuestionAnswer


def index(request):

	form = SubjectForm()

	if request.method == "POST":
		form = SubjectForm(request.POST)
		if form.is_valid():
			text = "Just generated questions by AI"

			return render(request, "main/index.html", {"form": form, "text": text})

	return render(request, "main/index.html", {"form": form	})


def all_questions(request):

	questions = QuestionAnswer.objects.all()

	return render(request, "main/questions.html", {"questions": questions})


def ask_question(request):

	form = QuestionAnswerForm()

	if request.method == "POST":
		form = QuestionAnswerForm(request.POST)
		if form.is_valid():
			question = form.cleaned_data["question"]
			answer = "random text generated by AI. Here is answer on user's question"

			QuestionAnswer.objects.create(
				question=question,
				answer=answer,
			)

			return redirect("questions")

	return render(request, "main/ask_question.html", {"form": form})

	