from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_list_or_404
from .models import User
 

@csrf_exempt
def say_hello(request):
    # return HttpResponse("Hello world")
    if request.method == 'POST':
        api_token = request.POST.get('api_token')
        if api_token:
            user = get_list_or_404(user)
            response_data = {'user_exists' : True,'message':'User found'}
        else:
            response_data = {'user_exists' : False,'message':'User found'}
    else:
        response_data = {'error' : 'Invalid http method'}           
    # return render(request,'index.html',{ 'name' : 'Sibaath'})
    return JsonResponse(response_data)

def home(request):
    if request.method == 'GET':
        return render(request,'index.html')

    

# Create your views here.
