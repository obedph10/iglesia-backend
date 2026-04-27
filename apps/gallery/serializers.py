from rest_framework import serializers
from .models import GalleryCategory, GalleryImage


class GalleryCategorySerializer(serializers.ModelSerializer):
    image_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = GalleryCategory
        fields = ["id", "name", "slug", "order", "image_count"]


class GalleryImageSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source="category.name", read_only=True, default="")

    class Meta:
        model = GalleryImage
        fields = [
            "id", "title", "description", "image", "category",
            "category_name", "order", "created_at",
        ]
