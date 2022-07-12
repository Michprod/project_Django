from django.contrib import admin
from django.urls import path
from .views import hello,home,FilmDetail

urlpatterns = [
    path('hello/<str:name>',hello),
    path('',home,name='film-home'),
    path('film/<int:pk>',FilmDetail.as_view(),name ='film-detail')
]
