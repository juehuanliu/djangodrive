# Generated by Django 3.0.4 on 2020-03-16 19:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile_usertext'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
