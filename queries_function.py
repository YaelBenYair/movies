import os
import django
import datetime

from django.db.models import Q, Count, Avg, Min, Max

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"
django.setup()

from movies_app.models import *

def get_younger_than(age: int):
    """
    Get all the actors in the db who are younger than {age} years old
    :param age: int
    :return:
    """
    age_year = datetime.datetime.now().year - age
    act = Actor.objects.filter(birth_year__gt=age_year)
    print(act)

def get_lt_time_gt_year(hours: float, release_year: int):
    """
    Get movies that last less than {time} hours and were released after {yaer}
    :param hours: in format 2.5 -> 2:hours, 5:minutes
    :param release_year: int
    :return:
    """


    pass




if __name__ == '__main__':
    # get_younger_than(50)
    # get_lt_time_gt_year(2.5, 2005)

    # 2
    for i in Movie.objects.filter(duration_in_min__lt=150, release_year__gt=2017):
        print(i)

    # 3
    print(Movie.objects.filter(Q(movie_name__icontains="no") | Q(movie_name__icontains="and")))

    # 4
    print(Movie.objects.filter(duration_in_min__lt=150, release_year__lt=2016))

    # 5
    actor = Actor.objects.annotate(nums_movies=Count('movie'))
    for ac in actor:
        print(ac, ac.nums_movies)

    # 6
    print(Rating.objects.aggregate(Avg('rating'), Max('rating'), Min('rating')))

    # 7
    for m in Movie.objects.annotate(avg_rating=Avg('rating__rating')):
        print(m, m.avg_rating)

    # 8
    print(Rating.objects.values_list('movie__movie_name', 'rating', 'rating_date').filter(rating_date__year=2023))

    # 9
    ac = Actor.objects.annotate(mini=Min('movie__rating__rating'), maxi=Max('movie__rating__rating'))
    for a in ac:
        print(a, a.mini, a.maxi)

    # 10
    mo = Movie.objects.annotate(avg_selery=Avg('movieactor__salary'))
    for m in mo:
        print(m, m.avg_selery)

    # 11
    ac = Actor.objects.annotate(avg_selery=Avg('movieactor__salary'))
    for a in ac:
        print(a, a.avg_selery)

    # 12
    ac = Actor.objects.filter(movieactor__main_role=True).values('name').annotate(main_role=Count('movieactor__main_role'))
    print(ac)

    #13
    m = Movie.objects.filter(movieactor__main_role=True).values('movie_name').annotate(actor=Count('actors'))
    print(m)







