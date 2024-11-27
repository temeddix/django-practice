from django.http import HttpRequest, HttpResponse


def index(request: HttpRequest):
    return HttpResponse("Hello, world. You're at the polls index.")


def detail(request: HttpRequest, question_id: int):
    return HttpResponse(f"You're looking at question {question_id}.")


def results(request: HttpRequest, question_id: int):
    response = f"You're looking at the results of question {question_id}."
    return HttpResponse(response)


def vote(request: HttpRequest, question_id: int):
    return HttpResponse(f"You're voting on question {question_id}.")
