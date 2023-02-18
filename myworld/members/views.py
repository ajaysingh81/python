from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import loader
from .models import Member

def index(request):
    return HttpResponse("Hello, world . you are at the index.")

def about(request):
    return HttpResponse("Hello, world . you are at the about.")

def temp(request):
    template = loader.get_template('index.html')
    return HttpResponse(template.render())
 
def members(request):
    mymembers = Member.objects.all().values()
    template = loader.get_template("allMembers.html")
    context = {
        'mymembers' : mymembers,
    }
    return HttpResponse(template.render(context, request))

def details(request,id):
    mymember = Member.objects.get(id = id)
    template = loader.get_template("details.html")
    context = {
        'mymember' : mymember,
    }
    return HttpResponse (template.render(context,request))