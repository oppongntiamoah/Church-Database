from django.contrib import admin
from .models import Member, Attendance, Visitor


admin.site.register(Member)
admin.site.register(Attendance)
admin.site.register(Visitor)