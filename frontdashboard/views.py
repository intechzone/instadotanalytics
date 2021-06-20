from django.shortcuts import render , redirect
from django.template import loader
from django.http import HttpResponse

# Create your views here.

#index
def frontindex(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
