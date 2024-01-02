# Generated by Django 4.2 on 2023-12-30 03:51

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_profile_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uuid',
            field=models.CharField(default=uuid.UUID('ba4b1776-c65f-49c1-89a7-ed5bed3d6ace'), max_length=300, verbose_name='uid'),
        ),
    ]