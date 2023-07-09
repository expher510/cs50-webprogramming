from django.shortcuts import render
import datetime

# Create your views here.
def index(requst):
   return render(requst,'newyear/index.html',{
      'bool':datetime.date.month==1 and datetime.date.day
   })



