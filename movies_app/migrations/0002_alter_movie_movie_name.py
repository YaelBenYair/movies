# Generated by Django 4.1.5 on 2023-01-29 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='movie_name',
            field=models.CharField(db_column='movie_name', db_index=True, max_length=256),
        ),
    ]