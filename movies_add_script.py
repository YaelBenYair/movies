import os

os.environ["DJANGO_SETTINGS_MODULE"] = "movies.settings"

import django

django.setup()

from movies_app.models import *

# movie_name, description, duration_in_min, release_year, pic_url, actors

if __name__ == '__main__':
    pass
    # Movie(movie_name='Captain America: Civil War',
    #       description='Political pressure mounts to install a system of accountability when the actions of the '
    #                   'Avengerslead to collateral damage',
    #       duration_in_min='135', release_year=2016,
    #       pic_url='https://resizing.flixster.com/3FsqAde5UAaQHTucsT5xtFRMHBw=/206x305/v2/https://resizing.flixster'
    #               '.com/nBBa8qH9lC0v5zJgtpLUwp9W92g=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzllZThmOGM5LTVjZmUtNDQ'
    #               '5Yy04ZjdjLTcyOWEzZWI0N2FlZC53ZWJw').save()
    #
    # Movie(movie_name='Doctor Strange',
    #       description="Dr. Stephen Strange's (Benedict Cumberbatch) life changes after a car accident robs him of the use "
    #                   "of his hands. When traditional medicine fails him, he looks for healing, and hope, in a mysterious "
    #                   "enclave",
    #       duration_in_min='93', release_year=2016,
    #       pic_url='https://resizing.flixster.com/35FB4rNQ8DhnEGwwzx4KpAyN6RI=/206x305/v2/https://resizing.flixster.com/'
    #               'vK77TbbXQYgkJ2HpvPp1p_W0tj4=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL2FkNDZiMzU2LTFmYTQtNDgwMS1iOWM5LTgxNTg2'
    #               'NDMxNjBmNi53ZWJw').save()
    #
    # Movie(movie_name='Guardians of the Galaxy Vol. 2',
    #       description='Peter Quill and his fellow Guardians are hired by a powerful alien race, the Sovereign, to protect'
    #                   ' their precious batteries from invaders',
    #       duration_in_min='135', release_year=2017,
    #       pic_url='https://resizing.flixster.com/k4IP-GZob9_6CobWh7mptITzdCw=/206x305/v2/https://'
    #               'flxt.tmsimg.com/NowShowing/152514/152514_aa.jpg').save()
    #
    # Movie(movie_name='Spider-Man: Homecoming',
    #       description='Thrilled by his experience with the Avengers, young Peter Parker returns home to '
    #                   'live with his Aunt May',
    #       duration_in_min='133', release_year=2017,
    #       pic_url='https://resizing.flixster.com/1MIZSkkmMlEyvrTmQUdie-CbXsQ=/206x305/v2/https://flxt.tmsimg.com'
    #               '/assets/p12798844_p_v8_ao.jpg').save()
    #
    # Movie(movie_name='Thor: Ragnarok',
    #       description='Imprisoned on the other side of the universe, the mighty Thor finds himself in a deadly gladiatorial'
    #                   ' contest that pits him against the Hulk, his former ally and fellow Avenger',
    #       duration_in_min='130', release_year=2017,
    #       pic_url='https://resizing.flixster.com/JuiNcQBYggEOrN5PbIVv0fq7SJA=/206x305/v2/https://flxt.tmsimg.'
    #               'com/assets/p12402331_p_v8_ax.jpg').save()
    #
    # Movie(movie_name='Black Panther',
    #       description="After the death of his father, T'Challa returns home to the African nation of Wakanda to take "
    #                   "his rightful place as king",
    #       duration_in_min='134', release_year=2018,
    #       pic_url='https://resizing.flixster.com/z27vZVXCRmpvETmdJQEW9Il7Z2Y=/206x305/v2/https://resizing.flixster.com'
    #               '/KBlur3LaA-y1U1yt6_Y2uO25ozA=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzLzMxOGI1YzBhLWMyMjEtNGUxMS1iM2Q0LWQ'
    #               '4OGMyYzQyZjQyYS53ZWJw').save()
    #
    # Movie(movie_name='Black Widow',
    #       description="In Marvel Studios' action-packed spy thriller 'Black Widow', Natasha Romanoff aka Black Widow "
    #                   "confronts the darker parts of her ledger when a dangerous conspiracy with ties to her past arises",
    #       duration_in_min='133', release_year=2021,
    #       pic_url='https://resizing.flixster.com/EyahmtqNmxs6zwn-bK1q9fmfiyA=/206x305/v2/https://'
    #               'resizing.flixster.com/UqanC4hHIFolYIKoZ020-YmubCQ=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL'
    #               'zRkMWJjZjI2LWE0MDktNDczZC05ZmNiLTIzMTQ0NTE5MGJiMC5qcGc=').save()
    #
    # Movie(movie_name='Thor: Love and Thunder',
    #       description="'Thor: Love and Thunder' finds Thor (Chris Hemsworth) on a journey unlike anything he's "
    #                   "ever faced -- a quest for inner peace",
    #       duration_in_min='123', release_year=2022,
    #       pic_url='https://resizing.flixster.com/biXtr85Fn_B1JDf4Xc9c6ntbU_A=/206x305/v2/https://resizing.flixster.com/zs'
    #               '8TFWbPfSsndNJWCpNiILwzf3o=/ems.cHJkLWVtcy1hc3NldHMvbW92aWVzL2JiYzJkMmE5LTllZDUtNDQ0Ny1hYmUxLTBmMzk1MDQ'
    #               '4M2NkNC5qcGc=').save()
    #
    # Movie(movie_name='Spider-Man: No Way Home',
    #       description="For the first time in the cinematic history of Spider-Man, "
    #                   "our friendly neighborhood hero's identity is revealed",
    #       duration_in_min='148', release_year=2021,
    #       pic_url='https://resizing.flixster.com/wouDuoTzmfpwzvVDiTldrBHkbTo=/'
    #               '206x305/v2/https://resizing.flixster.com/8PNiwC2bpe9OecfYZSOVkvYC5vk=/ems.'
    #               'cHJkLWVtcy1hc3NldHMvbW92aWVzL2U5NGM0Y2Q1LTAyYTItNGFjNC1hNWZhLWMzYjJjOTdjMTFhOS5qcGc=').save()

    # Actor(name='Chris Hemsworth', birth_year=1983).save()  # thor
    # Actor(name='Natalie Portman', birth_year=1981).save()  # thor
    # Actor(name='Benedict Cumberbatch', birth_year=1976).save()  # Strange
    # Actor(name='Rachel McAdams', birth_year=1978).save()  # Strange
    # Actor(name='Tom Holland', birth_year=1996).save()  # Spider-Man
    # Actor(name='Zendaya', birth_year=1996).save()  # Spider-Man
    # Actor(name='Scarlett Johansson', birth_year=1984).save()  # Widow

    # m = Movie.objects.get(id=1)
    # a = Actor.objects.get(id=5)
    # a2 = Actor.objects.get(id=7)
    # MovieActor(actor=a, movie=m, salary=500_000, main_role=False).save()
    # MovieActor(actor=a2, movie=m, salary=400_000, main_role=False).save()
    #
    # m2 = Movie.objects.get(id=2)
    # a3 = Actor.objects.get(id=3)
    # a4 = Actor.objects.get(id=4)
    # MovieActor(actor=a3, movie=m2, salary=1_000_300, main_role=True).save()
    # MovieActor(actor=a4, movie=m2, salary=400_300, main_role=False).save()
    #
    # m3 = Movie.objects.get(id=4)
    # a6 = Actor.objects.get(id=6)
    # MovieActor(actor=a, movie=m3, salary=1_000_600, main_role=True).save()
    # MovieActor(actor=a6, movie=m3, salary=600_000, main_role=False).save()
    #
    # m4 = Movie.objects.get(id=5)
    # a7 = Actor.objects.get(id=1)
    # a8 = Actor.objects.get(id=2)
    # MovieActor(actor=a7, movie=m4, salary=1_000_800, main_role=True).save()
    # MovieActor(actor=a8, movie=m4, salary=400_000, main_role=False).save()
    #
    # m5 = Movie.objects.get(id=8)
    # MovieActor(actor=a7, movie=m5, salary=1_000_800, main_role=True).save()
    # MovieActor(actor=a8, movie=m5, salary=1_000_900, main_role=True).save()
    #
    # m6 = Movie.objects.get(id=7)
    # MovieActor(actor=a2, movie=m6, salary=1_000_800, main_role=True).save()
    #
    # m7 = Movie.objects.get(id=9)
    # MovieActor(actor=a, movie=m7, salary=1_000_600, main_role=True).save()
    # MovieActor(actor=a6, movie=m7, salary=600_000, main_role=False).save()

    for i in range(2, 10):
        m = Movie.objects.get(id=i)
        Rating(movie=m, rating=9).save()


























