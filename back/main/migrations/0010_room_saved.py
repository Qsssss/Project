# Generated by Django 3.0.5 on 2020-04-27 19:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_room_people'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='saved',
            field=models.BooleanField(default=True),
        ),
    ]
