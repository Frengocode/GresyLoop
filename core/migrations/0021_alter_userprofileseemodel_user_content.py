# Generated by Django 4.2.11 on 2024-03-17 10:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_userprofileseemodel_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileseemodel',
            name='user_content',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='core.contentuploud_model'),
        ),
    ]
