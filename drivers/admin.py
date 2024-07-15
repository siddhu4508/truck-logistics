from django.contrib import admin
from .models import Driver


class DriverAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',
                    'license_number', 'identity_card_number')
    search_fields = ('first_name', 'last_name',
                     'license_number', 'identity_card_number')
    filter_horizontal = ('supervisors',)

admin.site.register(Driver, DriverAdmin)