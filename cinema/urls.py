from django.urls import path
from cinema.views import create_actors, created_Movies, read_actors, read_movie

urlpatterns = [
    path('actors/create/', create_actors),
    path('actors/<int:pk>/', read_actors),
    path('movie/create/', created_Movies),
    path('movie/<int:pk>', read_movie),
]