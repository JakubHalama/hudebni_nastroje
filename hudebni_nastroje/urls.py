from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static  # <-- přidá obsluhu statických souborů (nastroje)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('nastroje/', include('nastroje.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
