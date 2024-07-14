from django.shortcuts import render, get_object_or_404
from .models import InventoryItem


def inventory_list(request):
    items = InventoryItem.objects.all()
    return render(request, 'inventory/inventory_list.html', {'items': items})


def inventory_detail(request, item_id):
    item = get_object_or_404(InventoryItem, id=item_id)
    return render(request, 'inventory/inventory_detail.html', {'item': item})
