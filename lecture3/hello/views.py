# from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(requst):
    return render(requst,"hello/index.html")


def greet(requst,name):
    return render(requst,'hello/greet.html',{
        'name': name.capitalize()
    })