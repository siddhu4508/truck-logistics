from django.shortcuts import render, get_object_or_404
from .models import Driver


def driver_list(request):
    drivers = Driver.objects.all()
    return render(request, 'drivers/driver_list.html', {'drivers': drivers})


def driver_detail(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    return render(request, 'drivers/driver_detail.html', {'driver': driver})
