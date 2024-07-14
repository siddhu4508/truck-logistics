from django.shortcuts import render, get_object_or_404
from .models import MaintenanceRecord


def maintenance_list(request):
    records = MaintenanceRecord.objects.all()
    return render(request, 'maintenance/maintenance_list.html', {'records': records})


def maintenance_detail(request, record_id):
    record = get_object_or_404(MaintenanceRecord, id=record_id)
    return render(request, 'maintenance/maintenance_detail.html', {'record': record})
