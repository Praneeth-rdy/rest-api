
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

# Project imports
from . import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('webapp/', include('webapp.urls')),
]

# Adding staticfiles to path
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Adding media files to path
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)