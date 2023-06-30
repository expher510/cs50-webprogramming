from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

tasks =['foo','baar','street']

def index(request):
    return render(request,'task.html',
    {
       'task':tasks
    }
       )


def add(request):
    return render(request,'add.html')


def dav(request):
 return HttpResponse('dav')