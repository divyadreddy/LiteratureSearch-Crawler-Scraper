from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def landing(request):
	return render(request,'landing.html')
	# return HttpResponse("Hello, world. You're at the polls index.")

def acm(request):
	return render(request,'ACM.html')

def ieee(request):
	return render(request,'IEEE.html')

def sciencedirect(request):
	return render(request,'ScienceDirect.html')

def springer(request):
	return render(request,'Springer.html')