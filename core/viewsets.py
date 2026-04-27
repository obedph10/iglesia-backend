from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly


class BaseReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
  permission_classes = [IsAuthenticatedOrReadOnly]
  serializer_list_class = None
  serializer_detail_class = None

  def get_serializer_class(self):
    if self.action == "list" and self.serializer_list_class:
      return self.serializer_list_class
    return self.serializer_detail_class or self.serializer_class
