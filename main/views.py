from django.http.response import HttpResponse
from django.shortcuts import render
from .models import TODOLIST


def homepage(request):
    return render(request, "index28.html")

def test(request):
    todo_list = TODOLIST.objects.all()
    return render(request, "test.html", {"todo_list": todo_list} )

def second(request):
    return HttpResponse("test 2 page")

# Create your views here.
