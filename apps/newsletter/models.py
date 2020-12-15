from django.db import models
from apps.account.models import MyUser


class Newsletter(models.Model):
    to = models.CharField(max_length=150)
    msg = models.CharField(max_length=300)
    via = models.CharField(max_length=50)
    sms_id = models.CharField(max_length=150)
    date_sent = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.to
    

