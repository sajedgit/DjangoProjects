from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myView(request):
    return HttpResponse("Hello World!")


def aaa(request):
    name="sajed"
    return HttpResponse("This is Hello World! from uuu aaa and done by <b>{}</b>".format(name))