from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def myAppView(request):
    return HttpResponse("This is the App View!")

def hello(request):
   text = """<h1>welcome to my app !</h1>"""
   return HttpResponse(text)


# def helloTemplate(request):
#    return render(request, "myapp/template/hello.html", {})