# Generated by Django 4.2.11 on 2024-03-17 08:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_message_sender_delete_addfiend'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileseemodel',
            name='user_content',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='core.contentuploud_model'),
            preserve_default=False,
        ),
    ]