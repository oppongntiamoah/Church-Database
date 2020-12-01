from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

#! Event Table
class Event(models.Model):

    EVENT_TYPE_CHOICES = [
        ('Business Talk', 'Business Talk'),
        ('Relationship', 'Relationship'),
        ('Training', 'Training'),
        ('Conference', 'Conference'),
        ('Wedding', 'Wedding'),
        ('Child Dedication', 'Child Dedication'),
        ('Church Service', 'Church Service'),
        ('Prayer Time', 'Prayer Time'),
        ('Music Festival', 'Music Festival'),
    ]

    name = models.CharField(unique=True, max_length=150)
    event_type = models.CharField(choices=EVENT_TYPE_CHOICES, max_length=25)
    description = models.CharField(blank=True, null=True, max_length=255)
    creator = models.ForeignKey(User, on_delete=models.PROTECT)

    def __str__(self):
        return self.name 
    
    