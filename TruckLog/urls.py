from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),  # Main index URL
    path('users/', include('users.urls')),
    path('vehicles/', include('vehicles.urls')),
    path('drivers/', include('drivers.urls')),
    path('trips/', include('trips.urls')),
    path('inventory/', include('inventory.urls')),
    path('billing/', include('billing.urls')),
    path('dispatch/', include('dispatch.urls')),
    path('tracking/', include('tracking.urls')),
    path('maintenance/', include('maintenance.urls')),
    path('reports/', include('reports.urls')),
    path('fuel/', include('fuel.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
