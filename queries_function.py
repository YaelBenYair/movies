import os
import django
import datetime

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
    get_younger_than(50)
    get_lt_time_gt_year(2.5, 2005)