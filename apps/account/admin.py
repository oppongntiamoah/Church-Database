from django.contrib import admin
from django.contrib.auth.models import Group
from .models import MyUser, Config

admin.site.register(Config)
admin.site.register(MyUser)
admin.site.unregister(Group)