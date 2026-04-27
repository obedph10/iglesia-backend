from django.contrib import admin
from .models import DonationOption, Donation


@admin.register(DonationOption)
class DonationOptionAdmin(admin.ModelAdmin):
    list_display = ["label", "payment_method", "is_active", "order"]
    list_editable = ["is_active", "order"]
    list_filter = ["payment_method", "is_active"]


@admin.register(Donation)
class DonationAdmin(admin.ModelAdmin):
    list_display = ["donor_name", "amount", "payment_method", "status", "created_at"]
    list_filter = ["status", "payment_method"]
    search_fields = ["donor_name", "donor_email", "transaction_id"]
    readonly_fields = ["transaction_id", "created_at"]
