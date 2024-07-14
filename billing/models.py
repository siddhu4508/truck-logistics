from django.db import models


class Billing(models.Model):
    invoice_number = models.CharField(max_length=50, unique=True)
    vehicle_number = models.CharField(max_length=20)
    driver_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=100, choices=[
        ('transport', 'Transport'),
        ('maintenance', 'Maintenance'),
        ('fuel', 'Fuel'),
        ('other', 'Other'),
    ])
    billing_date = models.DateField()
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_status = models.CharField(max_length=20, choices=[
        ('paid', 'Paid'),
        ('pending', 'Pending'),
        ('canceled', 'Canceled'),
    ])
    remarks = models.TextField(blank=True)

    def __str__(self):
        return f"Invoice {self.invoice_number} - {self.service_type} - {self.total_amount}"
