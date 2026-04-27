from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "date", "time", "category", "order", "published"]
    list_editable = ["order", "published"]
    list_filter = ["category", "published"]
    search_fields = ["title", "description"]
    date_hierarchy = "date"
    fieldsets = (
        ("Información", {
            "fields": ("title", "description", "image", "location")
        }),
        ("Detalles", {
            "fields": ("date", "time", "end_date", "category", "registration_link")
        }),
        ("Organización", {
            "fields": ("order",)
        }),
        ("Estado", {
            "fields": ("published",)
        }),
    )
