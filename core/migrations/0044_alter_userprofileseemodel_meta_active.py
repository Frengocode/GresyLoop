# Generated by Django 4.2.11 on 2024-03-21 08:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_activemeta_alter_userprofileseemodel_meta_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileseemodel',
            name='meta_active',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='get_meta_activet_user', to='core.activemeta'),
        ),
    ]
