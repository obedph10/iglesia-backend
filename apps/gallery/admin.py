from django.contrib import admin
from .models import GalleryCategory, GalleryImage


@admin.register(GalleryCategory)
class GalleryCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "order"]
    list_editable = ["order"]
    prepopulated_fields = {"slug": ("name",)}


@admin.register(GalleryImage)
class GalleryImageAdmin(admin.ModelAdmin):
    list_display = ["thumbnail_preview", "title", "category", "order", "published", "created_at"]
    list_editable = ["category", "order", "published"]
    list_filter = ["category", "published", "created_at"]
    search_fields = ["title", "description"]
    readonly_fields = ["created_at", "thumbnail_preview"]
    fieldsets = (
        ("Información", {
            "fields": ("title", "description", "image", "thumbnail_preview")
        }),
        ("Organización", {
            "fields": ("category", "order")
        }),
        ("Estado", {
            "fields": ("published",)
        }),
        ("Metadatos", {
            "fields": ("created_at",),
            "classes": ("collapse",)
        }),
    )
    actions = ["mark_published", "mark_unpublished"]

    def thumbnail_preview(self, obj):
        if obj.image:
            return f'<img src="{obj.image.url}" style="max-width: 150px; max-height: 150px;" />'
        return "Sin imagen"
    thumbnail_preview.short_description = "Vista previa"
    thumbnail_preview.allow_tags = True

    def mark_published(self, request, queryset):
        updated = queryset.update(published=True)
        self.message_user(request, f"{updated} imagen(es) marcada(s) como publicada(s).")
    mark_published.short_description = "Marcar como publicado"

    def mark_unpublished(self, request, queryset):
        updated = queryset.update(published=False)
        self.message_user(request, f"{updated} imagen(es) marcada(s) como no publicada(s).")
    mark_unpublished.short_description = "Marcar como no publicado"
