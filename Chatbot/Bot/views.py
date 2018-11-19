from django.shortcuts import render, HttpResponse

#from django.views.static.serve()
from .models import Question
# Create your views here.
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import requests
import json

def home(request):
    return render(request, 'chat.html')

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    output = ', '.join([q.question_text for q in latest_question_list])
    return HttpResponse(output)