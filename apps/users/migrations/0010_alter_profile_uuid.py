# Generated by Django 4.2 on 2023-12-28 11:59

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_alter_otpcode_code_alter_profile_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='uuid',
            field=models.CharField(default=uuid.UUID('1b30f044-bffd-4506-b7af-21ec64510104'), max_length=300, verbose_name='uid'),
        ),
    ]