from django.contrib import admin
from django.urls import path
from app import views
urlpatterns = [
    path('', views.index, name='index.html'),
    path('register', views.register, name='register.html'),
    path('log_in', views.log_in, name='log_in'),
    path('dashboard', views.dashboard, name='dashboard'),
    path('log_out/', views.log_out, name='log_out.html'),
]
