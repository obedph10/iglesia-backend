from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from .models import DonationOption, Donation
from .serializers import DonationOptionSerializer, DonationSerializer


class DonationOptionViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = DonationOption.objects.filter(is_active=True)
    serializer_class = DonationOptionSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class DonationViewSet(viewsets.ModelViewSet):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer

    def get_permissions(self):
        if self.action in ("create",):
            self.permission_classes = [permissions.AllowAny]
        else:
            self.permission_classes = [permissions.IsAdminUser]
        return super().get_permissions()
