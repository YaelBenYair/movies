from django.urls import path

from . import views

urlpatterns = [
    path('api/movies', views.movies_list),
    path('api/movies/<int:movie_id>', views.movie_details),
    path('api/movies/<int:movie_id>/actors', views.movie_actors),
    path('', views.index, name='index'),
    path('api/ratings', views.get_ratings),
    path('api/actors', views.create_actor),
    path('api/actors/<int:actor_id>', views.update_actor),
    path('api/actors/<int:actor_id>/movies/<int:movie_id>', views.remove_from_movie),
    path('api/movies/<int:movie_id>/ratings', views.add_rating),
    path('api/ratings/<int:rating_id>', views.delete_movie_rating)
]