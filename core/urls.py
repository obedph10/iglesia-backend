from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/pages/", include("apps.pages.urls")),
    path("api/sermons/", include("apps.sermons.urls")),
    path("api/events/", include("apps.events.urls")),
    path("api/gallery/", include("apps.gallery.urls")),
    path("api/donations/", include("apps.donations.urls")),
    path("api/alliances/", include("apps.alliances.urls")),
    path("api/contact/", include("apps.contact.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

# Serve media files always — whitenoise handles static; media needs Django serving in demo
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
