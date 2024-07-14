from django.db import models
from trips.models import Trip  # Assuming you have a Trip model
from vehicles.models import Vehicle  # Assuming you have a Vehicle model


class TripReport(models.Model):
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE)
    total_distance = models.FloatField()
    total_time = models.DurationField()
    fuel_consumed = models.FloatField()  # in liters
    report_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Report for Trip {self.trip.id} on {self.report_date}"
