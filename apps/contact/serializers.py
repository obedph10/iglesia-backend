from rest_framework import serializers
from .models import SiteSettings, ContactMessage, PrayerRequest

class SiteSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = SiteSettings
        fields = [
            "address", "phone", "email", "google_maps_url", "schedule",
            "mission", "vision", "about_us", "our_faith", "faith_declaration",
            "home_title", "home_subtitle",
            "home_pillar_1_title", "home_pillar_1_desc",
            "home_pillar_2_title", "home_pillar_2_desc",
            "home_pillar_3_title", "home_pillar_3_desc",
            "home_pillar_4_title", "home_pillar_4_desc",
            "donations_bible_verse", "donations_bible_reference", "donations_why_donate",
            "facebook_url", "instagram_url", "youtube_url", "tiktok_url",
        ]

class ContactMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactMessage
        fields = "__all__"

class PrayerRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = PrayerRequest
        fields = "__all__"
