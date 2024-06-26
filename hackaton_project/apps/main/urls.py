from django.urls import path

from . import views


urlpatterns = [
    path("index", views.index, name="index"),
    path("ask_question", views.ask_question, name="ask_question"),
    path("questions", views.all_questions, name="questions"),
]