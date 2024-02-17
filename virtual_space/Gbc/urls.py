from django.urls import path
from . import views

urlpatterns = {
    path('check_user/',views.say_hello,name='check_user')
    ,path('',views.home)
}
