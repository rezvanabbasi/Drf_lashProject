# Generated by Django 4.2 on 2024-01-09 14:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0027_alter_profile_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uuid',
            field=models.CharField(default=uuid.UUID('41fe69ed-4d29-4797-ba69-f7cbb0afb4e6'), max_length=300, verbose_name='uid'),
        ),
    ]
