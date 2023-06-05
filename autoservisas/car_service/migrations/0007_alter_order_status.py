# Generated by Django 4.2.1 on 2023-06-04 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car_service', '0006_rename_cover_car_pictures'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(blank=True, choices=[(0, 'new'), (1, 'processing'), (2, 'complete'), (3, 'cancelled')], default=0, help_text='Statusas', max_length=1, verbose_name='status'),
        ),
    ]
