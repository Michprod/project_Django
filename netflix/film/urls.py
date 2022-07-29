from django.contrib import admin
from django.urls import path
from .views import (
        hello,
        home,
        FilmDetail,
        add_favorite_film,
        mylist_film,
        remove_favorite_film,
        liker,
        FilmCreateView,
        FilmUpdateView,
        FilmDeleteView
)

urlpatterns = [
    path('hello/<str:name>',hello),
    path('',home,name='film-home'),
    path('film/<int:pk>',FilmDetail.as_view(),name ='film-detail'), 
    path('film-new/',FilmCreateView.as_view(),name ='film-new'),
    path('film/<int:pk>/update',FilmUpdateView.as_view(),name ='film-update'), 
    path('film/<int:pk>/delete',FilmDeleteView.as_view(),name ='film-delete'), 
    path('film-add-favorite/<int:film_id>',add_favorite_film,name ="add-favorite-film"),
    path('film-remove-favorite/<int:film_id>',remove_favorite_film,name ="remove-favorite-film"),
    path('liker/<int:film_id>',liker,name ="liker"),
    path('mylist/',mylist_film,name ="mylist"),
    
]
