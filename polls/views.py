from django.http import HttpRequest, HttpResponse

from .models import Question


def index(request: HttpRequest):
    latest_question_list = Question.objects.order_by("-pub_date")[:5]
    output = ", ".join([q.question_text for q in latest_question_list])
    return HttpResponse(output)


def detail(request: HttpRequest, question_id: int):
    return HttpResponse(f"You're looking at question {question_id}.")


def results(request: HttpRequest, question_id: int):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request: HttpRequest, question_id: int):
    return HttpResponse(f"You're voting on question {question_id}.")
