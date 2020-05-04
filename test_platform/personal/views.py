from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def say_hello(request):
    name = request.GET.get("name","null")
    return HttpResponse("hello " + name)