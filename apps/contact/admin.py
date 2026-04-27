from django.contrib import admin
from .models import ContactMessage, PrayerRequest, SiteSettings


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "subject", "is_read", "created_at"]
    list_editable = ["is_read"]
    list_filter = ["is_read"]
    search_fields = ["name", "email", "subject", "message"]


@admin.register(PrayerRequest)
class PrayerRequestAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "is_private", "is_answered", "created_at"]
    list_editable = ["is_answered"]
    list_filter = ["is_private", "is_answered"]
    search_fields = ["name", "prayer_request"]

@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ["__str__", "address", "phone", "email"]
    
    fieldsets = (
        ("Información General de Contacto", {
            "fields": ("address", "phone", "email", "google_maps_url", "schedule")
        }),
        ("Redes Sociales", {
            "fields": ("facebook_url", "instagram_url", "youtube_url", "tiktok_url")
        }),
        ("Página: Inicio (Home)", {
            "fields": (
                "home_title", "home_subtitle",
                "home_pillar_1_title", "home_pillar_1_desc",
                "home_pillar_2_title", "home_pillar_2_desc",
                "home_pillar_3_title", "home_pillar_3_desc",
                "home_pillar_4_title", "home_pillar_4_desc"
            ),
            "classes": ("collapse",)
        }),
        ("Página: Quiénes Somos / Misión y Visión", {
            "fields": ("mission", "vision", "about_us", "our_faith", "faith_declaration"),
            "classes": ("collapse",)
        }),
        ("Página: Donaciones", {
            "fields": ("donations_bible_verse", "donations_bible_reference", "donations_why_donate"),
            "classes": ("collapse",)
        }),
    )

    def has_add_permission(self, request):
        # Prevent creating multiple settings
        if self.model.objects.exists():
            return False
        return super().has_add_permission(request)
