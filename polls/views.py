from django.db.models import F, QuerySet
from django.http import HttpResponseRedirect, HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse
from django.views import generic, View

from .models import Choice, Question


class IndexView(generic.ListView):
    template_name = "polls/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions."""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "polls/detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "polls/results.html"


class VoteView(View):
    def post(self, request: HttpRequest, question_id: int) -> HttpResponse:
        question = get_object_or_404(Question, pk=question_id)
        try:
            choice_set: QuerySet[Choice] = getattr(question, "choice_set")
            selected_choice = choice_set.get(pk=request.POST["choice"])
        except (KeyError, Choice.DoesNotExist):
            # Redisplay the question voting form with an error message.
            return render(
                request,
                "polls/detail.html",
                {
                    "question": question,
                    "error_message": "You didn't select a choice.",
                },
            )
        else:
            # Increment the vote count for the selected choice.
            selected_choice.votes = F("votes") + 1
            selected_choice.save()
            # Redirect to the results page after processing the vote.
            return HttpResponseRedirect(reverse("polls:results", args=(question_id,)))
