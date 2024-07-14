from django.db import models
from vehicles.models import Vehicle  # Assuming you have a Vehicle model


class Trip(models.Model):
    vehicle = models.ForeignKey(Vehicle, on_delete=models.CASCADE)
    destination = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    # Allow null for ongoing trips
    end_time = models.DateTimeField(null=True, blank=True)
    distance = models.FloatField(help_text="Distance in kilometers")
    driver_name = models.CharField(max_length=50)

    def __str__(self):
        return f"Trip to {self.destination} using {self.vehicle.registration_number}"
