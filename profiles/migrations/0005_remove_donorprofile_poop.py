# Generated by Django 2.0.3 on 2018-04-02 00:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0004_donorprofile_poop'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='donorprofile',
            name='poop',
        ),
    ]
