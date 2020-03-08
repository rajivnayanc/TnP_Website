from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'why_us_and_procedure'
urlpatterns = [
    path('why_us/',views.why_us,name='why_us'),
    path('procedure/',views.procedure,name='procedure'),
]