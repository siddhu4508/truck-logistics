from django.shortcuts import render, get_object_or_404
from .models import FuelTransaction


def fuel_list(request):
    transactions = FuelTransaction.objects.all()
    return render(request, 'fuel/fuel_list.html', {'transactions': transactions})


def fuel_detail(request, transaction_id):
    transaction = get_object_or_404(FuelTransaction, id=transaction_id)
    return render(request, 'fuel/fuel_detail.html', {'transaction': transaction})
