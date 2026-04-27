from django.contrib import admin
from .models import Alliance, AllianceProject


class AllianceProjectInline(admin.TabularInline):
    model = AllianceProject
    extra = 1


@admin.register(Alliance)
class AllianceAdmin(admin.ModelAdmin):
    list_display = ["name", "is_active", "created_at"]
    list_editable = ["is_active"]
    search_fields = ["name"]
    inlines = [AllianceProjectInline]


@admin.register(AllianceProject)
class AllianceProjectAdmin(admin.ModelAdmin):
    list_display = ["title", "alliance", "impact_category", "start_date", "is_active"]
    list_editable = ["is_active"]
    list_filter = ["impact_category", "alliance", "is_active"]
    search_fields = ["title", "description"]
