from rest_framework import generics, viewsets
from rest_framework.response import Response
from django.conf import settings
from django.core.cache import cache
from .models import SiteSettings, ContactMessage, PrayerRequest
from .serializers import SiteSettingsSerializer, ContactMessageSerializer, PrayerRequestSerializer
from .tasks import send_contact_emails

_SITE_SETTINGS_CACHE_KEY = "site_settings_singleton"


def _get_church_email() -> str:
    cached = cache.get(_SITE_SETTINGS_CACHE_KEY)
    if cached:
        return cached.get("email") or settings.DEFAULT_FROM_EMAIL
    try:
        obj = SiteSettings.objects.get(id=1)
        cache.set(_SITE_SETTINGS_CACHE_KEY, {"email": obj.email}, timeout=3600)
        return obj.email or settings.DEFAULT_FROM_EMAIL
    except SiteSettings.DoesNotExist:
        return settings.DEFAULT_FROM_EMAIL


class SiteSettingsView(generics.RetrieveAPIView):
    queryset = SiteSettings.objects.all()
    serializer_class = SiteSettingsSerializer

    def get_object(self):
        cached = cache.get(_SITE_SETTINGS_CACHE_KEY)
        if cached and isinstance(cached, SiteSettings):
            return cached
        obj, _ = SiteSettings.objects.get_or_create(id=1)
        cache.set(_SITE_SETTINGS_CACHE_KEY, obj, timeout=3600)
        return obj


class ContactMessageViewSet(viewsets.ModelViewSet):
    queryset = ContactMessage.objects.all()
    serializer_class = ContactMessageSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        if response.status_code == 201:
            church_email = _get_church_email()
            send_contact_emails.delay(dict(response.data), church_email)
        return response


class PrayerRequestViewSet(viewsets.ModelViewSet):
    queryset = PrayerRequest.objects.all()
    serializer_class = PrayerRequestSerializer
