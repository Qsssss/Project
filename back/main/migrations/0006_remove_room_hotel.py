# Generated by Django 3.0.5 on 2020-04-27 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0005_auto_20200427_2327'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='hotel',
        ),
    ]
