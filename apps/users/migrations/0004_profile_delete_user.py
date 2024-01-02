# Generated by Django 4.2 on 2023-12-28 04:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('users', '0003_alter_user_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=255, unique=True)),
                ('phone_number', models.CharField(max_length=11, unique=True)),
                ('password', models.CharField(max_length=8, null=True)),
                ('full_name', models.CharField(max_length=300, null=True)),
                ('image', models.ImageField(null=True, upload_to='')),
                ('address', models.CharField(max_length=300, null=True)),
                ('birth_date', models.DateField(null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('uuid', models.CharField(default=uuid.UUID('f633c06f-de70-49e4-a367-4232284c6664'), max_length=300, verbose_name='uid')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
                ('user_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='user', to='users.usertype')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
        ),
        migrations.DeleteModel(
            name='User',
        ),
    ]