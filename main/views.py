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

def add_tomeet(request):
    form = request.POST
    text = form["tomeet_text"]
    tomeet = ToMeet(text=text)
    tomeet.save()
    return redirect(meeting)

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

# Create your views here.
