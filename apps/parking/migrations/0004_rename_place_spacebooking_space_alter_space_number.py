# Generated by Django 4.0 on 2021-12-13 16:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('parking', '0003_rename_placebooking_spacebooking'),
    ]

    operations = [
        migrations.RenameField(
            model_name='spacebooking',
            old_name='place',
            new_name='space',
        ),
        migrations.AlterField(
            model_name='space',
            name='number',
            field=models.PositiveIntegerField(unique=True),
        ),
    ]
