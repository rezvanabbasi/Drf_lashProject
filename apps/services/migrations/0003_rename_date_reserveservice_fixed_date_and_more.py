# Generated by Django 4.2 on 2023-12-30 05:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0002_lashservice_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='reserveservice',
            old_name='date',
            new_name='fixed_date',
        ),
        migrations.RemoveField(
            model_name='reserveservice',
            name='is_available',
        ),
        migrations.AddField(
            model_name='reserveservice',
            name='comment',
            field=models.TextField(max_length=300, null=True),
        ),
    ]
