# Generated by Django 4.2 on 2023-12-28 07:27

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0008_otpcode_alter_profile_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otpcode',
            name='code',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='profile',
            name='uuid',
            field=models.CharField(default=uuid.UUID('c6e7c11a-264f-4a87-83a7-9135ce67a30a'), max_length=300, verbose_name='uid'),
        ),
    ]
