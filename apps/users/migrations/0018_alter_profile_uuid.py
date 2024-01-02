# Generated by Django 4.2 on 2023-12-30 06:21

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0017_alter_profile_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uuid',
            field=models.CharField(default=uuid.UUID('fc5bda9c-de7e-44f9-acba-a48a698db4ae'), max_length=300, verbose_name='uid'),
        ),
    ]