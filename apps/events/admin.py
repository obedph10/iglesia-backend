from django.contrib import admin
from .models import Event


@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ["title", "date", "time", "category", "featured", "published"]
    list_editable = ["featured", "published"]
    list_filter = ["category", "featured", "published"]
    search_fields = ["title", "description"]
    date_hierarchy = "date"
