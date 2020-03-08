from django.contrib import admin
from django.urls import path, include
from . import views

app_name='IAM'
urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>/',views.detail,name='event_detail'),
    path('<int:id>/speakers/',views.speakerlist,name='event_speakers'),
    path('<int:id>/speakers/<int:speaker_id>/',views.speakerDetail,name='event_speakerDetail'),
]