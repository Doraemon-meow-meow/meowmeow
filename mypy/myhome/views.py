from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
	return render(request,'myhome/index.html')
def list(request):

	return HttpResponse('list')
	return render(request,'myhome/list .html')

def info(request):

	return HttpResponse('info')

def login(request):

	return HttpResponse('login')

def register(request):

	return HttpResponse('register')