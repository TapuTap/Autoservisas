# Generated by Django 4.2.1 on 2023-06-04 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_service', '0004_order_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='cover',
            field=models.ImageField(blank=True, null=True, upload_to='car_service/car_pictures', verbose_name='pictures'),
        ),
    ]
