from django.shortcuts import render
from .mail import send_mail
from django.http import HttpResponse

# Create your views here.

def home_view(request):
    num = send_mail() 
    if num == 1 :
        return HttpResponse('<h1>ERROR</h1>') 
    return HttpResponse('<h1>Sent</h1>')

