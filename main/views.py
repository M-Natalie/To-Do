from django.http.response import HttpResponse
from django.shortcuts import render


def homepage(request):
    return HttpResponse("Hello World!")

def test(request):
    return render(request, "test.html")

# Create your views here.
