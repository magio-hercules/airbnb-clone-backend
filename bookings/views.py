from rest_framework.viewsets import ModelViewSet
from .models import Booking
from .serializers import BookingSerializer


class BookingViewSet(ModelViewSet):
    serializer_class = BookingSerializer
    queryset = Booking.objects.all()
