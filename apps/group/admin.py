from django.contrib import admin
from .models import Group, GroupMember, MemRole


class GroupMemberInline(admin.TabularInline):
    model = GroupMember
    extra = 1
    

@admin.register(Group)
class GroupAdmin(admin.ModelAdmin):
    list_display = ('group_name', 'group_description')
    filter_horizontal = ('group_members', )
    inlines = [GroupMemberInline, ]


admin.site.register(MemRole)