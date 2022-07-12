from django.contrib import admin
from django.urls import path
from .views import filmDetail, hello,home,filmDetail

urlpatterns = [
    path('hello/<str:name>',hello),
    path('',home,name='film-home'),
    path('film/<int:pk>',filmDetail,name ='film-detail')
]
