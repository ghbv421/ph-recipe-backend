from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('recipes.urls')), # Includes Task 2 & 4 routes
]

# Task 3: Serve media files when in development mode
if settings.DEBUG:
    # Maps the URL /assets/images/ to the folder mobile_app/assets/images
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)