# Generated by Django 5.0.7 on 2024-07-14 14:01

from django.db import migrations, models
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('vehicles', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vehicle',
            name='last_maintenance_date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='vehicle',
            name='purchase_date',
            field=models.DateField(null=True, blank=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='capacity',
            field=models.FloatField(help_text='Capacity in tons'),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='registration_number',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]