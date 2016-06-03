from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.views import generic

from .models import Question, Choice

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'questions'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')

class DetailView(generic.DetailView):
    template_name = 'polls/detail.html'
    model = Question

class ResultView(generic.DetailView):
    template_name = 'polls/results.html'
    model = Question

# Create your views here.
def index(request):
    questions = Question.objects.order_by('-pub_date')
    return render(request, 'polls/index.html', {'questions': questions})


def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist) as e:
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': str(e)
        })
    else:
        selected.votes += 1
        selected.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

# def vote2(request, question_id, choice_id):
#     return HttpResponse("You are voting for the question %s with choice %s" % (question_id, choice_id))
