# Generated by Django 4.2.11 on 2024-03-16 09:33

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_alter_comment_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileseemodel',
            name='subscribers',
            field=models.ManyToManyField(blank=True, null=True, related_name='subscribes', to=settings.AUTH_USER_MODEL),
        ),
    ]
