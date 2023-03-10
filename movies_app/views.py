from django.shortcuts import render, get_object_or_404
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from movies_app.models import Movie
from movies_app.serializers import *


# Create your views here.

# ---------------------------------------- api/movies ------------------------------------------------------------------

def get_movie_list(request):
    movies_qs = Movie.objects.all()

    if 'name' in request.query_params:
        movies_qs = movies_qs.filter(movie_name__iexact=request.query_params['name'])
    if 'duration_from' in request.query_params:
        movies_qs = movies_qs.filter(duration_in_min__gte=request.query_params['duration_from'])
    if 'duration_to' in request.query_params:
        movies_qs = movies_qs.filter(duration_in_min__lte=request.query_params['duration_to'])
    if 'description' in request.query_params:
        movies_qs = movies_qs.filter(description__icontains=request.query_params['description'])

    if not movies_qs:
        return Response(status=status.HTTP_204_NO_CONTENT)

    serializer = MovieSerializer(movies_qs, many=True)
    return Response(serializer.data)


def create_movie(request):
    serializer = MovieDetailSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):  # -> אם עושים את האקספשן TRUE אז הג'נגו מחזיר שגיאה אם המשתמש הכניס דברים לא נכונים
        serializer.create(serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

    pass

@api_view(['GET', 'POST'])
def movies_list(request):
    if request.method == 'GET':
        return get_movie_list(request)
    elif request.method == 'POST':
        return create_movie(request)

# ----------------------------------------------------------------------------------------------------------------------


# ------------------------------------ api/movies/<int:movie_id> -------------------------------------------------------

# option1

# @api_view(['GET'])
# def movie_details(request, movie_id: int):
#     try:
#         movie = Movie.objects.filter(id=movie_id)
#         serializer = MovieDetailSerializer(movie, many=False)
#         return Response(serializer.data)
#     except Movie.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)


# option2
@api_view(['GET'])
def movie_details(request, movie_id: int):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = MovieDetailSerializer(movie, many=False)
    return Response(serializer.data)

# ----------------------------------------------------------------------------------------------------------------------


# ------------------------------------ api/ratings ---------------------------------------------------------------------

@api_view(['GET'])
def get_ratings(request):
    rating_qs = Rating.objects.all()

    if 'rating_from' in request.query_params:
        rating_qs = rating_qs.filter(rating__gt=request.query_params['rating_from'])
    if 'rating_to' in request.query_params:
        rating_qs = rating_qs.filter(rating__lte=request.query_params['rating_to'])
    if 'release_year' in request.query_params:
        rating_qs = rating_qs.filter(movie__release_year__gt=request.query_params['release_year'])
    serializer = RatingSerializer(rating_qs, many=True)
    return Response(serializer.data)

# ----------------------------------------------------------------------------------------------------------------------


# ------------------------------------ api/movies/<int:movie_id>/actors ------------------------------------------------

@api_view(['GET', 'POST'])
def movie_actors(request, movie_id):
    if request.method == 'GET':
        movie_actors = MovieActor.objects.filter(movie_id=movie_id)
        serializer = MovieActorSerializer(movie_actors, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        get_object_or_404(Movie, id=movie_id)
        serializer = AddMovieActorSerializer(data=request.data, context={'movie_id': movie_id, 'request': request})
        if serializer.is_valid(raise_exception=True):
            serializer.create(serializer.validated_data)
        return Response()

# ----------------------------------------------------------------------------------------------------------------------


# ---------------------------------------- api/actors ------------------------------------------------------------------

@api_view(['POST'])
def create_actor(request):
    serializer = ActorSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.create(serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

# ----------------------------------------------------------------------------------------------------------------------



# ------------------------------------- api/actors/<int:actor_id> ------------------------------------------------------
@api_view(['PATCH', 'DELETE'])
def update_actor(request, actor_id):
    if request.method == 'PATCH':
        actor = get_object_or_404(Actor, id=actor_id)
        serializer = ActorSerializer(actor, data=request.data, partial=True, many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response()
    elif request.method == 'DELETE':
        actor = get_object_or_404(Actor, id=actor_id)
        actor.delete()
        return Response()

# ----------------------------------------------------------------------------------------------------------------------


# ---------------------------------- api/actors/<int:actor_id>/movies/<int:movie_id> -----------------------------------

@api_view(['DELETE', 'PATCH'])
def remove_from_movie(request, actor_id, movie_id):
    actor = get_object_or_404(Actor, id=actor_id)
    movie = get_object_or_404(Movie, id=movie_id)
    if request.method == 'DELETE':
        movieactor = get_object_or_404(MovieActor, movie=movie, actor=actor)
        movieactor.delete()
        return Response()
    elif request.method == 'PATCH':
        movieactor = get_object_or_404(MovieActor, movie_id=movie_id, actor_id=actor_id)
        serializer = UpdateMovieActorSerializer(movieactor, data=request.data, partial=True, many=False)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response()

# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- api/movies/<int:movie_id>/ratings --------------------------------------------------

@api_view(['POST'])
def add_rating(request, movie_id):
    movie = get_object_or_404(Movie, id=movie_id)
    serializer = AddRatingSerializer(data=request.data, context={'movie': movie, 'request': request})
    if serializer.is_valid(raise_exception=True):
        serializer.create(serializer.validated_data)
        return Response(status=status.HTTP_201_CREATED)

# ----------------------------------------------------------------------------------------------------------------------


# --------------------------------- api/ratings/<int:rating_id> --------------------------------------------------------

@api_view(['DELETE'])
def delete_movie_rating(request, rating_id):
    rating = get_object_or_404(Rating, id=rating_id)
    rating.delete()
    return Response()
    pass


def index(request):
    return render(request, 'index.html')




