from django.shortcuts import render
from django.http import HttpResponse

def say_hello(request):
    # return HttpResponse("Hello world")
    x=1
    y=1
    return render(request,'index.html',{ 'name' : 'Sibaath'})

# Create your views here.
