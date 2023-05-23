from rest_framework import serializers
from cinema.models import Actor, Movie

class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor, Movie
        fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    actors = serializers.StringRelatedField(many=True)
