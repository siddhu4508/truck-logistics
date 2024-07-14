from django.db import models


class FuelTransaction(models.Model):
    FUEL_TYPE_CHOICES = [
        ('diesel', 'Diesel'),
        ('petrol', 'Petrol'),
        ('gasoline', 'Gasoline'),
    ]

    fuel_type = models.CharField(max_length=20, choices=FUEL_TYPE_CHOICES)
    vehicle_number = models.CharField(max_length=20)
    date = models.DateField()
    quantity = models.DecimalField(
        max_digits=10, decimal_places=2)  # Quantity in liters
    mileage_kms = models.PositiveIntegerField()  # Mileage in kilometers
    payment_method = models.CharField(max_length=50)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    rate_per_liter = models.DecimalField(max_digits=10, decimal_places=2)
    receipt_image = models.ImageField(upload_to='receipts/')
    remarks = models.TextField(blank=True)
    driver_name = models.CharField(max_length=100)
    supervisor_name = models.CharField(max_length=100)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.fuel_type} - {self.vehicle_number} - {self.driver_name} - {self.timestamp}"
