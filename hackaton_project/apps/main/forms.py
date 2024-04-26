from django import forms

from .models import QuestionAnswer


class QuestionAnswerForm(forms.ModelForm):
	"""
		Form for creating Question
	"""
	class Meta:
		model = QuestionAnswer
		fields = ["question"]


class SubjectForm(forms.Form):
	"""
		Form for specify subject
	"""

	subject = forms.CharField(max_length=30)
