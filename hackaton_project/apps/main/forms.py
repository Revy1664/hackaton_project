from django import forms

from .models import QuestionAnswer


class QuestionAnswerForm(forms.ModelForm):

	class Meta:
		model = QuestionAnswer
		fields = ["question"]


class SubjectForm(forms.Form):
	subject = forms.CharField(max_length=30)
