from django.contrib import admin
from .models import Series, Sermon


@admin.register(Series)
class SeriesAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at"]
    search_fields = ["name"]


@admin.register(Sermon)
class SermonAdmin(admin.ModelAdmin):
    list_display = ["title", "speaker", "order", "date", "series", "published"]
    list_editable = ["order", "published"]
    list_filter = ["series", "speaker", "published"]
    search_fields = ["title", "speaker", "description"]
    date_hierarchy = "date"
    fieldsets = (
        ("Información", {
            "fields": ("title", "description", "speaker", "youtube_url", "image")
        }),
        ("Organización", {
            "fields": ("series", "order")
        }),
        ("Estado", {
            "fields": ("date", "published")
        }),
    )
