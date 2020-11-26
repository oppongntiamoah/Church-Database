from django.urls import path
from django.contrib.auth import views as auth_views
from . import views as v

urlpatterns = [
    path('', v.home, name="home"),
    path('installation/', v.config, name="install"),
    path('login/', auth_views.LoginView.as_view(), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]
