from rest_framework.viewsets import ModelViewSet
from .models import Wishlist
from .serializers import WishlistSerializer


class WishlistViewSet(ModelViewSet):
    serializer_class = WishlistSerializer
    queryset = Wishlist.objects.all()
