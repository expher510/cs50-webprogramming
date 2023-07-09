from django.shortcuts import render

# Create your views here.
tasks=['1','2',
       '3']
def index(requst):
    return render(requst,'tasks/index.html'
                  ,{"tasks":tasks})