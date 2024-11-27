from django.http import HttpRequest, HttpResponse, Http404
from django.shortcuts import render

from .models import Question


def index(request: HttpRequest):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    return render(
        request,
        "polls/index.html",
        {
            "latest_question_list": latest_question_list,
        },
    )


def detail(request: HttpRequest, question_id: int):
    try:
        question = Question.objects.get(pk=question_id)
    except Question.DoesNotExist:
        raise Http404("Question does not exist")
    return render(
        request,
        "polls/detail.html",
        {
            "question": question,
        },
    )


def results(request: HttpRequest, question_id: int):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request: HttpRequest, question_id: int):
    return HttpResponse(f"You're voting on question {question_id}.")
