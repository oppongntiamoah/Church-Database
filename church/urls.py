from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    
    # account
    path('', include('apps.account.urls')),

    # member
    #path('member/', include('apps.member.urls')),
]
