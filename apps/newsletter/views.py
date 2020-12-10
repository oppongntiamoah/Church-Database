from django.shortcuts import render
from apps.member.models import Member, Visitor
from django.core.mail import BadHeaderError, send_mail



def send_email(request):
    pass