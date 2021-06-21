from django.shortcuts import render , redirect
from django.template import loader
from django.http import HttpResponse


# Create your views here.

#index
def backindex(request):
    template = loader.get_template('studentindex.html')
    return HttpResponse(template.render())

def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())