from django.urls import path
from . import views as v

urlpatterns = [
    path('', v.MemberList.as_view(), name="member-list"),
    path('d/<pk>/', v.MemberDetailView.as_view(), name='member_detail'),
    path('new/', v.MemberCreateView.as_view(), name='member_create'),
]
