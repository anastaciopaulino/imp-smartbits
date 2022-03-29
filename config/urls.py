from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from config.views import Home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', Home.as_view(), name='index'),
    path('courses/', include('apps.courses.urls', namespace='courses')),
    path('events/', include('apps.events.urls', namespace='events')),
    path('gallery/', include('apps.gallery.urls', namespace='gallery')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)