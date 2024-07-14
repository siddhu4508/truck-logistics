from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models


class CustomUser(AbstractUser):
    USER_ROLES = (
        ('supervisor', 'Supervisor'),
        ('owner', 'Owner'),
        ('truck_vendor', 'Truck Vendor'),
        ('customer', 'Customer'),
    )
    role = models.CharField(
        max_length=20, choices=USER_ROLES, default='customer')

    groups = models.ManyToManyField(
        Group, related_name='customuser_set', blank=True)
    user_permissions = models.ManyToManyField(
        Permission, related_name='customuser_set', blank=True)

    def __str__(self):
        return self.username


class OwnerProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=100)
    company_address = models.TextField()
    contact_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.user.username} - {self.company_name}"


class SupervisorProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    department = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.department}"


class TruckVendorProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    company_name = models.CharField(max_length=100)
    service_area = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.user.username} - {self.company_name}"


class CustomerProfile(models.Model):
    user = models.OneToOneField(
        CustomUser, on_delete=models.CASCADE, primary_key=True)
    address = models.TextField()
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return self.user.username
