# Generated by Django 2.2 on 2021-07-29 23:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tvshows_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='desc',
            new_name='description',
        ),
    ]