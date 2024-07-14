from django.db import models

class Vehicle(models.Model):
    registration_number = models.CharField(max_length=15, unique=True)
    model = models.CharField(max_length=50)
    capacity = models.FloatField(help_text="Capacity in tons")
    availability_status = models.BooleanField(default=True)
    purchase_date = models.DateField(
        null=True, blank=True)  # Allow null or blank
    last_maintenance_date = models.DateField(
        null=True, blank=True)  # Allow null or blank

    def __str__(self):
        return self.registration_number
