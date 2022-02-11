# Generated by Django 3.0.5 on 2020-04-27 13:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200426_2207'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='bath_image',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='number_of_visitors',
            new_name='visitors',
        ),
        migrations.RemoveField(
            model_name='room',
            name='bed_image',
        ),
        migrations.AlterField(
            model_name='room',
            name='hotel',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Hotel'),
        ),
    ]