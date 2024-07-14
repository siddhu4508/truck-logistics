from django.shortcuts import render, get_object_or_404
from .models import TripReport


def report_list(request):
    reports = TripReport.objects.all()
    return render(request, 'reports/report_list.html', {'reports': reports})


def report_detail(request, report_id):
    report = get_object_or_404(TripReport, id=report_id)
    return render(request, 'reports/report_detail.html', {'report': report})
