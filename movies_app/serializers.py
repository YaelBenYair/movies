from rest_framework import serializers
from movies_app.models import *

# class MovieSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Movie
#         fields = '__all__'


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'movie_name', 'duration_in_min', 'release_year']


class MovieDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        exclude = ['actors']


class MovieNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['movie_name']


class RatingSerializer(serializers.ModelSerializer):
    # movie = serializers.StringRelatedField(many=False)
    movie = MovieNameSerializer()

    class Meta:
        model = Rating
        fields = '__all__'


class ActorNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['name']


class MovieActorSerializer(serializers.ModelSerializer):

    actor = serializers.StringRelatedField(many=False)  # לא מכונן
    # actor = ActorNameSerializer()  # מכונן

    class Meta:
        model = MovieActor
        # fields = '__all__'
        exclude = ['movie']
        depth = 1



