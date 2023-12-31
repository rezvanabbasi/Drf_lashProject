# Generated by Django 4.2 on 2023-12-30 04:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0014_alter_profile_uuid'),
    ]

    operations = [
        migrations.CreateModel(
            name='LashService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(null=True, upload_to='')),
                ('title', models.CharField(max_length=300)),
                ('material', models.TextField(max_length=300)),
                ('price', models.IntegerField()),
                ('duration', models.TimeField()),
                ('is_available', models.BooleanField(default=True)),
                ('staff', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='lash_service', to='users.profile')),
            ],
        ),
        migrations.CreateModel(
            name='ReserveService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('is_available', models.BooleanField(default=False)),
                ('customer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='customer', to='users.profile')),
                ('service', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reserve_service', to='services.lashservice')),
            ],
        ),
    ]
