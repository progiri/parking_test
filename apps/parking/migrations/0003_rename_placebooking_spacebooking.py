# Generated by Django 4.0 on 2021-12-13 12:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('parking', '0002_rename_place_space'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PlaceBooking',
            new_name='SpaceBooking',
        ),
    ]