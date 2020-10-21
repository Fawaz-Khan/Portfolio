from django.shortcuts import render
from django.http import HttpResponse

def home(request):
	return render(request,'profile.html')

def projects(request) :
    return render(request,'projects.html')

def certification(request) :
    return render(request,'certification.html')

def connect(request) :
    return render(request,'connect.html')
	
