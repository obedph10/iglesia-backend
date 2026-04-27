from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from django.db.models import Count, Q
from core.viewsets import BaseReadOnlyViewSet
from .models import Alliance, AllianceProject
from .serializers import (
    AllianceListSerializer,
    AllianceDetailSerializer,
    AllianceProjectSerializer,
)


class AllianceViewSet(BaseReadOnlyViewSet):
    queryset = Alliance.objects.filter(is_active=True)
    serializer_list_class = AllianceListSerializer
    serializer_detail_class = AllianceDetailSerializer

    def get_queryset(self):
        if self.action == "list":
            return Alliance.objects.filter(is_active=True).annotate(
                project_count=Count("projects", filter=Q(projects__is_active=True))
            )
        return Alliance.objects.filter(is_active=True).prefetch_related("projects")


class AllianceProjectViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = AllianceProject.objects.filter(is_active=True)
    serializer_class = AllianceProjectSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filterset_fields = ["impact_category", "alliance"]
    ordering_fields = ["-start_date"]
