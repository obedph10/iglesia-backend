from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import AllianceViewSet, AllianceProjectViewSet

router = DefaultRouter()
router.register(r"projects", AllianceProjectViewSet)
router.register(r"", AllianceViewSet, basename="alliance")

urlpatterns = [
    path("", include(router.urls)),
]
