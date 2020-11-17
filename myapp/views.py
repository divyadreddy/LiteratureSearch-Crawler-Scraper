from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
	return HttpResponse("Hello, world. You're at the polls index.")
	# return render(request,'templates/myapp/landing.html')

def acm(request):
	return HttpResponse("ACM page renders here")
