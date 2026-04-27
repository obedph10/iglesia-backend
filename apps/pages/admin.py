from django.contrib import admin
from .models import Page


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    list_display = ["title", "slug", "published", "order", "created_at"]
    list_editable = ["published", "order"]
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ["title", "content"]
    list_filter = ["published"]
