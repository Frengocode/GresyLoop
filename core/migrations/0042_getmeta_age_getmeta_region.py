# Generated by Django 4.2.11 on 2024-03-20 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0041_getmeta'),
    ]

    operations = [
        migrations.AddField(
            model_name='getmeta',
            name='age',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='getmeta',
            name='region',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
