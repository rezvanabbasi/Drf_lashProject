# Generated by Django 4.2 on 2023-12-30 06:45

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0018_alter_profile_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uuid',
            field=models.CharField(default=uuid.UUID('fdf9f72b-ede9-4bc3-8001-7561116dce7b'), max_length=300, verbose_name='uid'),
        ),
    ]