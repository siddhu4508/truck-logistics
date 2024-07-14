# Generated by Django 5.0.7 on 2024-07-14 14:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('trips', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tracking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('trip', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trips.trip')),
            ],
        ),
    ]
