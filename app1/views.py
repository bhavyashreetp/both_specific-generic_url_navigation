from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse


def tom(request):
    return HttpResponse('<h1>this is app1 string response</h1>')

def ankitha(request):
    return render(request,'ankitha.html')

 



