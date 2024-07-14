from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import CustomUser, OwnerProfile, SupervisorProfile, TruckVendorProfile, CustomerProfile


@receiver(post_save, sender=CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.role == 'owner':
            OwnerProfile.objects.create(user=instance)
        elif instance.role == 'supervisor':
            SupervisorProfile.objects.create(user=instance)
        elif instance.role == 'truck_vendor':
            TruckVendorProfile.objects.create(user=instance)
        elif instance.role == 'customer':
            CustomerProfile.objects.create(user=instance)


@receiver(post_save, sender=CustomUser)
def save_user_profile(sender, instance, **kwargs):
    if instance.role == 'owner':
        instance.ownerprofile.save()
    elif instance.role == 'supervisor':
        instance.supervisorprofile.save()
    elif instance.role == 'truck_vendor':
        instance.truckvendorprofile.save()
    elif instance.role == 'customer':
        instance.customerprofile.save()
