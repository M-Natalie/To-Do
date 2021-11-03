from django.http.response import HttpResponse
from django.shortcuts import render


def homepage(request):
    return HttpResponse("Hello World!")

def test(request):
    return render(request, "test.html")

def second(request):
    return HttpResponse("test 2 page")

# Create your views here.
