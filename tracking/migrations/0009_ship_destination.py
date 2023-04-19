# Generated by Django 4.2 on 2023-04-12 10:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tracking', '0008_create_ports'),
    ]

    operations = [
        migrations.AddField(
            model_name='ship',
            name='destination',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ships', to='tracking.port', verbose_name='Пункт назначения'),
        ),
    ]
