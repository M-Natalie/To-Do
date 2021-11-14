from typing import Text
from django.db.models.fields import TextField
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
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

def add_todo(request):
    form = request.POST
    text = form["todo_text"]
    todo = TODOLIST(text=text)
    todo.save()
    return redirect(test)



def delete_todo(request, id):
    todo = TODOLIST.objects.get(id=id)
    todo.delete()
    return redirect(test)

def mark_todo(request, id):
    todo = TODOLIST.objects.get(id=id)
    todo.is_favorite = True
    todo.save()
    return redirect(test)

def unmark_todo(request, id):
    todo = TODOLIST.objects.get(id=id)
    todo.is_favorite = False
    todo.save()
    return redirect(test)

def close_todo(request, id):
    todo = TODOLIST.objects.get(id=id)
    todo.is_closed = not todo.is_closed
    todo.save()
    return redirect(test)



def add_tomeet(request):
    form = request.POST
    person  = form["tomeet_person"]
    phone_number = form["tomeet_phone_number"]
    tomeet = ToMeet(person=person, phone_number=phone_number)
    tomeet.save()
    return redirect(meeting)

def delete_tomeet(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.delete()
    return redirect(meeting)

def marked_tomeet(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_favorite = True
    tomeet.save()
    return redirect(meeting)

def unmark_tomeet(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_favorite = False
    tomeet.save()
    return redirect(meeting)

def closed_tomeet(request, id):
    tomeet = ToMeet.objects.get(id=id)
    tomeet.is_closed = not tomeet.is_closed
    tomeet.save()
    return redirect(meeting) 

# Create your views here.
