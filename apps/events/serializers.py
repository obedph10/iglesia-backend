from rest_framework import serializers
from .models import Event


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id", "title", "date", "time", "location",
            "category", "image", "order", "created_at",
        ]


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id", "title", "description", "date", "time", "end_date",
            "location", "image", "category", "registration_link", "order",
            "published", "created_at",
        ]
