from rest_framework import serializers
from .models import Event


class EventListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id", "title", "date", "time", "location",
            "category", "image", "featured", "created_at",
        ]


class EventDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = [
            "id", "title", "description", "date", "time", "end_date",
            "location", "image", "category", "registration_link",
            "published", "featured", "created_at",
        ]
