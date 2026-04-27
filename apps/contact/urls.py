from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContactMessageViewSet, PrayerRequestViewSet, SiteSettingsView

router = DefaultRouter()
router.register(r"messages", ContactMessageViewSet)
router.register(r"prayer", PrayerRequestViewSet)

urlpatterns = [
    path("", include(router.urls)),
    path("settings/", SiteSettingsView.as_view(), name="site-settings"),
]
