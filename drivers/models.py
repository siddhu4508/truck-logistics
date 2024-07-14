from django.db import models


class Driver(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='drivers/')
    license_number = models.CharField(max_length=50)
    license_image = models.ImageField(upload_to='licenses/')
    identity_card_number = models.CharField(max_length=50)
    identity_card_image = models.ImageField(upload_to='identity_cards/')
    address = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
