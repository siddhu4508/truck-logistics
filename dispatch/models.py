from django.db import models


class Dispatch(models.Model):
    vehicle_number = models.CharField(max_length=20)
    driver_name = models.CharField(max_length=100)
    destination = models.CharField(max_length=255)
    dispatch_date = models.DateField()
    estimated_arrival_date = models.DateField()
    status = models.CharField(max_length=20, choices=[
        ('pending', 'Pending'),
        ('in_transit', 'In Transit'),
        ('delivered', 'Delivered'),
        ('canceled', 'Canceled'),
    ])
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"Dispatch {self.id} - {self.vehicle_number} to {self.destination}"
