from django.http import HttpResponse
from django.template import RequestContext, loader
from django.shortcuts import render

from django import forms

#from hitch.models import Driver, Client

def index(request):
	#latest_question_list = Question.objects.all().order_by('-pub_date')[:5]
    #context = {'latest_question_list': latest_question_list}
    #return render(request, 'polls/index.html')
    #template = loader.get_template('hitch/index.html')
    return render(request,'hitch/index.html')


def client(request):
	return render(request,'hitch/client.html')

def driver(request):
	return render(request,'hitch/driver.html')


