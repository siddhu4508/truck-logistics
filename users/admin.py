from django.contrib import admin
from .models import CustomUser, OwnerProfile, SupervisorProfile, TruckVendorProfile, CustomerProfile
from django.contrib.auth.admin import UserAdmin


class CustomUserAdmin(UserAdmin):
    model = CustomUser
    fieldsets = (
        *UserAdmin.fieldsets,
        (
            'Role',
            {
                'fields': ('role',)
            }
        ),
    )


admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(OwnerProfile)
admin.site.register(SupervisorProfile)
admin.site.register(TruckVendorProfile)
admin.site.register(CustomerProfile)
