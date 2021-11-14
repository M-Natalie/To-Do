from django.db import models


class TODOLIST(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class ToMeet(models.Model):
    person = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    data_of_meeting = models.DateTimeField(auto_created=True, null=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

    
class goal_for_month(models.Model):
        MONTH = (
            ('1', 'Январь'),
            ('2', 'Февральь'),
            ('3', 'Март'),
            ('4', 'Апрель'),
            ('5', 'Май'),
            ('6', 'Июнь'),
            ('7', 'Июль'),
            ('8', 'Август'),
            ('9', 'Сентябрь'),
            ('10', 'Октябрьрь'),
            ('11', 'Ноябрь'),
            ('12', 'Декабрь'),
        )
        goal = models.CharField(max_length=255)
        month = models.CharField(max_length=2, choices=MONTH)
        difficulty = models.SmallIntegerField()
        reason_for_goal = models.TextField() 
    

# Create your models here.
