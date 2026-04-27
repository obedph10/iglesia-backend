from core.viewsets import BaseReadOnlyViewSet
from .models import Event
from .serializers import EventListSerializer, EventDetailSerializer


class EventViewSet(BaseReadOnlyViewSet):
    queryset = Event.objects.filter(published=True)
    serializer_list_class = EventListSerializer
    serializer_detail_class = EventDetailSerializer
    filterset_fields = ["category", "featured"]
    search_fields = ["title", "description", "location"]
    ordering_fields = ["date", "created_at"]
