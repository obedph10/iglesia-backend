from core.viewsets import BaseReadOnlyViewSet
from .models import Page
from .serializers import PageListSerializer, PageDetailSerializer


class PageViewSet(BaseReadOnlyViewSet):
    queryset = Page.objects.filter(published=True)
    serializer_list_class = PageListSerializer
    serializer_detail_class = PageDetailSerializer
    lookup_field = "slug"
