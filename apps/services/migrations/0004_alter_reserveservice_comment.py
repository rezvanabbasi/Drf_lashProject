# Generated by Django 4.2 on 2023-12-30 06:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0003_rename_date_reserveservice_fixed_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reserveservice',
            name='comment',
            field=models.TextField(blank=True, max_length=300, null=True),
        ),
    ]
