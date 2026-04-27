from rest_framework import serializers
from .models import Series, Sermon


class SeriesSerializer(serializers.ModelSerializer):
    sermon_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = Series
        fields = ["id", "name", "description", "image", "sermon_count", "created_at"]


class SermonListSerializer(serializers.ModelSerializer):
    series_name = serializers.CharField(source="series.name", read_only=True, default="")

    class Meta:
        model = Sermon
        fields = [
            "id", "title", "speaker", "youtube_url", "date",
            "image", "series", "series_name", "created_at",
        ]


class SermonDetailSerializer(serializers.ModelSerializer):
    series_detail = SeriesSerializer(source="series", read_only=True)

    class Meta:
        model = Sermon
        fields = [
            "id", "title", "description", "speaker", "youtube_url",
            "date", "image", "series", "series_detail", "published", "created_at",
        ]
