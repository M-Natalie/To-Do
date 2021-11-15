from typing import Text
from django.db.models.fields import TextField
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from .models import TODOLIST, Habits, ToMeet, Habits


def homepage(request):
    return render(request, "index28.html")

def habit(request):
    habit_list = Habits.objects.all()
    return render(request, "habit.html", {"habit_list": habit_list} )

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
    date_of_meeting = form["tomeet_date_of_meeting"]
    tomeet = ToMeet(person=person, phone_number=phone_number, date_of_meeting=date_of_meeting)
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


    



def add_habit(request):
    form = request.POST
    name = form["habit_name"]
    comment = form["habit_comment"]
    habit = Habits(name=name, comment=comment)
    habit.save()
    return redirect("habit")



def delete_habit(request, id):
    habit = Habits.objects.get(id=id)
    habit.delete()
    return redirect("habit")

def marked_habit(request, id):
    habit = Habits.objects.get(id=id)
    habit.important = True
    habit.save()
    return redirect("habit")

def unmark_habit(request, id):
    habit = Habits.objects.get(id=id)
    habit.important = False
    habit.save()
    return redirect("habit")

def closed_habit(request, id):
    habit = Habits.objects.get(id=id)
    habit.done_for_today = not habit.done_for_today
    habit.save()
    return redirect("habit")
# Create your views here.
