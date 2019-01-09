from django.shortcuts import render
from django.http import HttpResponse, Http404
#from django.template import loader

from .models import Question

# Create your views here.
"""
def home(request):

    return render(request, 'base.html', {})
"""

def index(request):
    #return HttpResponse("Welcome to Math Practice!!!")
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    #output = ', '.join([q.question_text for q in latest_question_list])
    #template = loader.get_template('math_practiceapp/index.html')
    context = {
        'latest_question_list': latest_question_list,
        }
    #return HttpResponse(output)
    #return HttpResponse(template.render(context, request))
    return render(request, 'math_practice/index.html', context)

def detail(request, question_id):
    # TODO: try creating conext before in in try block to retain consistency of creating context before return and passing it in as an argument
    #try:
    #    question = Question.objects.get(pk=question_id)
    #except Question.DoesNotExist:
    #    raise Http404("Question does not exist")
    #return HttpResponse("You're looking at question %s." % question_id)
    #return render(request, 'math_practiceapp/detail.html', {'question': question})

    # trying get and raising 404 if it doesn't exist is common, so a relevant shortcut function was developed
    # first argument is the Django model, and then takes an arbitrary number of keyword arguments
    # get_list_or_404() is another helper function leveraging filter() instead of get()
    question = get_object_or_404(Question, pk=question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
