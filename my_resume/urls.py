
from django.contrib import admin
from django.urls import path, include
from my_resume import views

urlpatterns = [
    path('', views.home, name='home_page'),
    
]
