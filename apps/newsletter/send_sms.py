import os
from twilio.rest import Client
from django.conf import settings
from .models import Newsletter

account_sid = settings.TWILIO_ACCOUNT_SID
auth_token = settings.TWILIO_AUTH_TOKEN


def sendSMS(body, to, via):
    
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body=body,
        from_='+12059647805',
        to=to
    )

    Newsletter.objects.create(to=to, msg=body, via=via, sms_id=message.sid)

    print(message.sid)
