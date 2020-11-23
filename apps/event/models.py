from django.db import models


#! Event Type

class EventType(models.Model):

    EVENT_TYPE_STATUS = [
        ('w', 'Weekly'),
        ('m', 'Monthly'),
        ('y', 'Yearly'),
    ]

    name = models.CharField(unique=True, max_length=150)
    status = models.CharField(choices=EVENT_TYPE_STATUS, max_length=1)

    def __str__(self):
        return self.name
    

#! Event Table
class Event(models.Model):
    name = models.CharField(max_length=150)
    event_type = models.ForeignKey(EventType, blank=True, null=True, on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self):
        return self.name + " - " + self.date
    