from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GalleryCategoryViewSet, GalleryImageViewSet

router = DefaultRouter()
router.register(r"categories", GalleryCategoryViewSet)
router.register(r"images", GalleryImageViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
