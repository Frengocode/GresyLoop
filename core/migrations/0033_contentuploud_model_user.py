# Generated by Django 4.2.11 on 2024-03-18 10:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_remove_contentuploud_model_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contentuploud_model',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='content_uplouds_user', to=settings.AUTH_USER_MODEL),
        ),
    ]