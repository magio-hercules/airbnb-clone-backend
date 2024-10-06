from rest_framework.viewsets import ModelViewSet
from .models import Experience, Perk
from .serializers import ExperienceSerializer, PerkSerializer


class ExperienceViewSet(ModelViewSet):
    serializer_class = ExperienceSerializer
    queryset = Experience.objects.all()


class PerkViewSet(ModelViewSet):
    serializer_class = PerkSerializer
    queryset = Perk.objects.all()
