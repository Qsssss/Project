# Generated by Django 3.0.5 on 2020-04-27 18:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_room_hotel'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Manager',
        ),
        migrations.RemoveField(
            model_name='room',
            name='visitors',
        ),
    ]