from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Count, Q
from core.viewsets import BaseReadOnlyViewSet
from .models import Series, Sermon
from .serializers import SeriesSerializer, SermonListSerializer, SermonDetailSerializer


class SeriesViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Series.objects.annotate(
        sermon_count=Count("sermons", filter=Q(sermons__published=True))
    )
    serializer_class = SeriesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SermonViewSet(BaseReadOnlyViewSet):
    queryset = Sermon.objects.filter(published=True)
    serializer_list_class = SermonListSerializer
    serializer_detail_class = SermonDetailSerializer
    filterset_fields = ["series", "speaker"]
    search_fields = ["title", "description", "speaker"]
    ordering_fields = ["date", "created_at"]
