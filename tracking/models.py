from django.db import models
from vehicles.models import Vehicle  # Assuming you have a Vehicle model
from trips.models import Trip  # Assuming you have a Trip model


class Tracking(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    latitude = models.CharField(max_length=10)
    longitude = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Tracking for Trip {self.trip.id} at {self.timestamp}"
