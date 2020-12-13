from django.contrib import admin
from .models import Member, Attendance, Visitor


@admin.register(Member)
class MemberAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'date_joined', 'dob', 'address', 'phone_number', 'email',
        'date_added'
    )
    date_hierarchy = 'date_joined'
    search_fields = ('l_name', 'f_name', 'm_name')
    ordering = ('email', 'phone_number')

    

@admin.register(Visitor)
class VisitorAdmin(admin.ModelAdmin):
    list_display = (
        'full_name', 'date', 'age', 'address', 'phone_number', 'email',
        'status', 'reason', 'guest_of'
    )
    date_hierarchy = 'date'
    search_fields = ('l_name', 'f_name', 'm_name')
    ordering = ('email', 'phone_number')

    
@admin.register(Attendance)
class AttendanceAdmin(admin.ModelAdmin):
    list_display = ('event', 'date', 'men', 'women', 'children', 'visitors', 'total')
    list_editable = ('men', 'women', 'children', 'visitors')
    date_hierarchy = 'date'
    ordering = ('event',)
