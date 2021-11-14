from django.contrib import admin
from .models import TODOLIST, ToMeet, goal_for_month, Habits



admin.site.register(TODOLIST)
admin.site.register(ToMeet)
admin.site.register(goal_for_month)
admin.site.register(Habits)

# Register your models here.
