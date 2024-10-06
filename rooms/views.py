from rest_framework.viewsets import ModelViewSet
from .models import Room, Amenity
from .serializers import RoomSerializer, AmenitySerializer


class RoomViewSet(ModelViewSet):
    serializer_class = RoomSerializer
    queryset = Room.objects.all()


class AmenityViewSet(ModelViewSet):
    serializer_class = AmenitySerializer
    queryset = Amenity.objects.all()
