from rest_framework import serializers
from .models import DonationOption, Donation


class DonationOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DonationOption
        fields = [
            "id", "payment_method", "label", "description",
            "bank_name", "account_type", "account_number", "account_holder",
            "identification", "paypal_email", "card_image", "order",
        ]


class DonationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Donation
        fields = [
            "id", "amount", "donor_name", "donor_email",
            "payment_method", "transaction_id", "status", "message", "created_at",
        ]
        read_only_fields = ["status", "transaction_id", "created_at"]
