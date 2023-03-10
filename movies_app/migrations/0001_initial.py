# Generated by Django 4.1.5 on 2023-01-23 09:35

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('movie_name', models.CharField(db_column='movie_name', max_length=256)),
                ('description', models.TextField(db_column='description', null=True)),
                ('duration_in_min', models.FloatField(db_column='duration')),
                ('release_year', models.IntegerField(db_column='year', validators=[django.core.validators.MinValueValidator(1900), django.core.validators.MaxValueValidator(2050)])),
                ('pic_url', models.URLField(db_column='pic_url', max_length=512, null=True)),
            ],
            options={
                'db_table': 'movies',
            },
        ),
        migrations.CreateModel(
            name='Reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('review_text', models.TextField(db_column='review_text')),
                ('review_date', models.DateField(auto_now=True, db_column='rating_date')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='movies_app.movie')),
            ],
            options={
                'db_table': 'reviews',
            },
        ),
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rating', models.SmallIntegerField(db_column='rating', validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(11)])),
                ('rating_date', models.DateField(auto_now=True, db_column='rating_date')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='movies_app.movie')),
            ],
            options={
                'db_table': 'ratings',
            },
        ),
    ]
