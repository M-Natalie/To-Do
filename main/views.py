from django.http.response import HttpResponse
from django.shortcuts import render
from .models import TODOLIST, ToMeet


def homepage(request):
    return render(request, "index28.html")

def test(request):
    todo_list = TODOLIST.objects.all()
    return render(request, "test.html", {"todo_list": todo_list} )

def second(request):
    return HttpResponse("test 2 page")

def meeting(request):
    to_meet = ToMeet.objects.all()
    return render(request, "meeting.html", {"to_meet": to_meet} )

# Create your views here.
