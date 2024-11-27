from django.http import HttpRequest, HttpResponse
from django.shortcuts import render

from .models import Question


def index(request: HttpRequest):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    context = {"latest_question_list": latest_question_list}
    return render(request, "polls/index.html", context)


def detail(request: HttpRequest, question_id: int):
    return HttpResponse(f"You're looking at question {question_id}.")


def results(request: HttpRequest, question_id: int):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request: HttpRequest, question_id: int):
    return HttpResponse(f"You're voting on question {question_id}.")
