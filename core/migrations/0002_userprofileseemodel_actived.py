# Generated by Django 4.2.11 on 2024-03-15 19:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileseemodel',
            name='actived',
            field=models.BooleanField(default=False),
        ),
    ]
