# Generated by Django 5.0.7 on 2024-07-14 15:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dispatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('vehicle_number', models.CharField(max_length=20)),
                ('driver_name', models.CharField(max_length=100)),
                ('destination', models.CharField(max_length=255)),
                ('dispatch_date', models.DateField()),
                ('estimated_arrival_date', models.DateField()),
                ('status', models.CharField(choices=[('pending', 'Pending'), ('in_transit', 'In Transit'), ('delivered', 'Delivered'), ('canceled', 'Canceled')], max_length=20)),
                ('remarks', models.TextField(blank=True)),
            ],
        ),
    ]