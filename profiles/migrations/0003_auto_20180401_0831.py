# Generated by Django 2.0.3 on 2018-04-01 08:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0002_auto_20180401_0458'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donorprofile',
            name='location',
        ),
        migrations.RemoveField(
            model_name='donorprofile',
            name='role',
        ),
        migrations.AddField(
            model_name='donorprofile',
            name='zipcode',
            field=models.CharField(blank=True, max_length=5),
        ),
    ]