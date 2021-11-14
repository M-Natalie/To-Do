from django.contrib import admin
from .models import TODOLIST, ToMeet, goal_for_month



admin.site.register(TODOLIST)
admin.site.register(ToMeet)
admin.site.register(goal_for_month)

# Register your models here.
