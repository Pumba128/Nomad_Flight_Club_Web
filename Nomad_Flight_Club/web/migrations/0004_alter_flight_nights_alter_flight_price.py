# Generated by Django 4.1.4 on 2022-12-16 21:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_alter_flight_airlines_alter_flight_iata_city_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flight',
            name='nights',
            field=models.IntegerField(blank=True, default=0),
        ),
        migrations.AlterField(
            model_name='flight',
            name='price',
            field=models.IntegerField(blank=True, default=99999),
        ),
    ]
