from django.contrib import admin
from .models import Group, GroupMember, MemRole


admin.site.register(Group)
admin.site.register(MemRole)
admin.site.register(GroupMember)