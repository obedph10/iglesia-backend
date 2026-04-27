from django.urls import path
from .views import PageViewSet

list_view = PageViewSet.as_view({"get": "list"})
detail_view = PageViewSet.as_view({"get": "retrieve"})

urlpatterns = [
    path("", list_view, name="page-list"),
    path("<slug:slug>/", detail_view, name="page-detail"),
]
