# Generated by Django 4.2 on 2024-01-06 05:55

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_alter_profile_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uuid',
            field=models.CharField(default=uuid.UUID('ff7d2422-fcd1-4e42-857a-0197c1976c7f'), max_length=300, verbose_name='uid'),
        ),
    ]
