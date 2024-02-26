from django.contrib import admin
from django.urls import path, include
from .views import *

app_name = "article"

urlpatterns = [
    path('article/<int:id>', detail, name='detail'),
    path('', articles, name='articles'),
    
]