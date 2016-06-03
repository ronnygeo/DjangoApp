from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("Hello!!! You are in the polls section!")


def detail(request, question_id):
    return HttpResponse("You are in the detail view for the question %s" % question_id)


def results(request, question_id):
    return HttpResponse("You are in the results view for the question %s" % question_id)


def vote(request, question_id, choice_id):
    return HttpResponse("You are voting for the question %s with choice %s" % (question_id, choice_id))
