from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.core.mail import send_mail

# Create your views here.

def home(request):
    return render(request,('home.html'))

def coffee(request):
    return render(request,('coffee.html'))    


def contact(request):
    return render(request,('contact.html'))

def reservation(request):
    return render(request,('reservation.html'))


def error(request, exception=None):
    return render(request, 'error.html', status=404)