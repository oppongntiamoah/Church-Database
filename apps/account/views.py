from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from apps.member.models import Member, Visitor
from django.db.models import Count, Sum, F, Max
import datetime

@login_required
def dashboard(request):

    # date settings
    currentYear = datetime.datetime.now().year
    currentM = datetime.datetime.now().month
    prevYear = currentYear - 1
    month = str(datetime.datetime.now().strftime("%B")) + " " + str(currentYear)


    # TOTAL MEMEBERS AND VISITORS
    members = Member.objects.count()
    visitors = Visitor.objects.count()

    # TOTAL VISITORS THIS MONTH
    visit_month = Visitor.objects.filter(date__year=currentYear).filter(date__month=currentM).count()

    # gp = revenue - expenses

    context = {
        'members': members,
        'visitors': visitors,
        'visit_month': visit_month,
    }
    return render(request, 'index.html', context)
