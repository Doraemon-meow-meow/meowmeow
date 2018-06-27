from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def hou(request):

	return render(request,'hou/index.html')
