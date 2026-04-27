from rest_framework import serializers
from .models import Alliance, AllianceProject


class AllianceProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = AllianceProject
        fields = [
            "id", "title", "description", "image", "impact_category",
            "start_date", "end_date", "location", "volunteers_needed",
            "is_active", "created_at",
        ]


class AllianceListSerializer(serializers.ModelSerializer):
    project_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Alliance
        fields = ["id", "name", "logo", "website", "project_count", "created_at"]


class AllianceDetailSerializer(serializers.ModelSerializer):
    projects = AllianceProjectSerializer(many=True, read_only=True)

    class Meta:
        model = Alliance
        fields = [
            "id", "name", "description", "logo", "website",
            "is_active", "projects", "created_at",
        ]
