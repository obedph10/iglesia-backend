from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Count, Q
from core.viewsets import BaseReadOnlyViewSet
from .models import GalleryCategory, GalleryImage
from .serializers import GalleryCategorySerializer, GalleryImageSerializer


class GalleryCategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = GalleryCategory.objects.annotate(
        image_count=Count("images", filter=Q(images__published=True))
    )
    serializer_class = GalleryCategorySerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    lookup_field = "slug"


class GalleryImageViewSet(BaseReadOnlyViewSet):
    queryset = GalleryImage.objects.filter(published=True)
    serializer_class = GalleryImageSerializer
    filterset_fields = ["category", "featured"]
    ordering_fields = ["-created_at"]
