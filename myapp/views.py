from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse
import os

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

def receive_data(request):
	print("basic = ",request.POST['basic'])
	return sendDownloadedFile()

def sendDownloadedFile():
	path = os.getcwd()+"/output.json"
	print("Sending file...")
	response = FileResponse(open('manage.py', 'rb'),as_attachment=True)
	return response