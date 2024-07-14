from django.shortcuts import render, get_object_or_404
from .models import Vehicle


def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'vehicles/vehicle_list.html', {'vehicles': vehicles})


def vehicle_detail(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, id=vehicle_id)
    return render(request, 'vehicles/vehicle_detail.html', {'vehicle': vehicle})
