from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from . import views

urlpatterns = [
    path('signin/', views.login , name='login'), 
    path('signup/', views.register, name='register'),
    path('warga/', views.warga, name='warga'),
    path('biodata/', views.setting, name='biodata'),
    path('settings/', views.edit_profile, name='setting'),
    path('logout/', views.logout, name='logout')
        ]
