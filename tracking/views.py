from django.shortcuts import render, get_object_or_404
from .models import Tracking
from trips.models import Trip  # Assuming you need to reference Trip


def tracking_list(request):
    trackings = Tracking.objects.all()
    return render(request, 'tracking/tracking_list.html', {'trackings': trackings})


def tracking_detail(request, tracking_id):
    tracking = get_object_or_404(Tracking, id=tracking_id)
    return render(request, 'tracking/tracking_detail.html', {'tracking': tracking})
