from django.contrib import admin
from django.urls import path, include
from . import views
app_name = 'placements'
urlpatterns = [
    path('<int:id>/',views.index,name='index')
]