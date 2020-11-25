from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

#! Event Table
class Event(models.Model):

    EVENT_TYPE_CHOICES = [
        ('w', 'Weekly'),
        ('m', 'Monthly'),
        ('y', 'Yearly'),
    ]

    name = models.CharField(unique=True, max_length=150)
    event_type = models.CharField(choices=EVENT_TYPE_CHOICES, max_length=1)
    description = models.CharField(blank=True, null=True, max_length=255)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name 
    
    