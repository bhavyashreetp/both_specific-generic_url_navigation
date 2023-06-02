from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
 
def chutki(request):
    return HttpResponse('<h1>this is app3 string response</h1>')
def sri(request):
    return render(request,'sri.html')