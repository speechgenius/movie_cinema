# Generated by Django 5.0.1 on 2024-01-24 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0004_alter_movie_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='trailer',
            field=models.CharField(default='', max_length=100),
        ),
    ]