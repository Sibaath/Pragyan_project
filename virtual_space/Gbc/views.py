from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_list_or_404
from .models import User
 


def say_hello(request):
    # return HttpResponse("Hello world")
    if request.method == 'POST':
        api_token = request.POST.get('api_token')
        if api_token:
            
            
    return render(request,'index.html',{ 'name' : 'Sibaath'})

# Create your views here.
