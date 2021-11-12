from django.db import models


class TODOLIST(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class ToMeet(models.Model):
    person = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    data_of_meeting = models.DateField()
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

# Create your models here.
