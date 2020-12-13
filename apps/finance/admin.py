from django.contrib import admin
from .models import *


@admin.register(Contribution)
class ContributionAdmin(admin.ModelAdmin):
    list_display = ('member', 'contribution_type', 'amount', 'date_received', 'note')
    autocomplete_fields = ('member', 'contribution_type')


@admin.register(Contribution_Type)
class Contribution_TypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_active', 'start_date', 'end_date', 'note')
    search_fields = ('name',)
    list_filter = ('is_active','start_date')
    

@admin.register(Offertory)
class OffertoryAdmin(admin.ModelAdmin):
    list_display = ('event', 'amount', 'date_received')
    list_filter = ('event','date_received')
    date_hierarchy = 'date_received'


@admin.register(Giving)
class GivingAdmin(admin.ModelAdmin):
    list_display = ('member', 'amount', 'date_received', 'note')
    date_hierarchy = 'date_received'

    def save_model(self, request, obj, form, change):
        obj.note = request.user
        super().save_model(request, obj, form, change)


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'phone_number', 'email', 'date_received', 'occupation', 'amount','note')
    date_hierarchy = 'date_received'


@admin.register(Tithe)
class TitheAdmin(admin.ModelAdmin):
    list_display = ('member', 'amount', 'month', 'date_received', 'note')
    date_hierarchy = 'date_received'
    ordering = ('member',)
    list_filter = ('month', )
