from django.shortcuts import render, get_object_or_404
from .models import Billing


def billing_list(request):
    billings = Billing.objects.all()
    return render(request, 'billing/billing_list.html', {'billings': billings})


def billing_detail(request, billing_id):
    billing = get_object_or_404(Billing, id=billing_id)
    return render(request, 'billing/billing_detail.html', {'billing': billing})
