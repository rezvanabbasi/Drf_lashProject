# Generated by Django 4.2 on 2024-01-06 11:23

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0025_alter_profile_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uuid',
            field=models.CharField(default=uuid.UUID('05192825-6698-432a-a931-2af7462fba85'), max_length=300, verbose_name='uid'),
        ),
    ]
