from django.shortcuts import render, get_object_or_404
from .models import Dispatch


def dispatch_list(request):
    dispatches = Dispatch.objects.all()
    return render(request, 'dispatch/dispatch_list.html', {'dispatches': dispatches})


def dispatch_detail(request, dispatch_id):
    dispatch = get_object_or_404(Dispatch, id=dispatch_id)
    return render(request, 'dispatch/dispatch_detail.html', {'dispatch': dispatch})
