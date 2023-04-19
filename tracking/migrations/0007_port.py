# Generated by Django 4.2 on 2023-04-12 10:13

from django.db import migrations, models
import django_countries.fields


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0006_alter_ship_image_alter_ship_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Port',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20, verbose_name='Название')),
                ('code', models.CharField(max_length=10, unique=True, verbose_name='Код')),
                ('latitude', models.DecimalField(decimal_places=15, max_digits=20, verbose_name='Широта')),
                ('longitude', models.DecimalField(decimal_places=15, max_digits=20, verbose_name='Долгота')),
                ('country', django_countries.fields.CountryField(max_length=2, verbose_name='Страна')),
            ],
        ),
    ]
