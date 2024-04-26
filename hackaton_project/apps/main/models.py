from django.db import models


class QuestionAnswer(models.Model):
	question = models.TextField(verbose_name="Вопрос")
	answer = models.TextField(verbose_name="Ответ")

	def __str__(self):
		return self.question
