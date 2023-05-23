from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from cinema.models import Actor, Movie
from cinema.serializers import ActorSerializer, MovieSerializer

@api_view(['POST'])
def create_actors(request):
    serializer = ActorSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def read_actors(request, pk):
    try:
        actor = Actor.objects.get(pk=pk)
        serializer = ActorSerializer(actor)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    except Actor.DoesNotExist:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['POST'])
def created_Movies(request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def read_movie(request, pk):
    try:
        movie = Movie.objects.get(pk=pk)
        serializer = MovieSerializer(movie)
        return Response(serializer.data, status=status.HTTP_200_OK)
    except Movie.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
