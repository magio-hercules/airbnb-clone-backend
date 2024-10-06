from rest_framework.viewsets import ModelViewSet
from .models import Tweet, Like
from .serializers import TweetSerializer, LikeSerializer


class TweetViewSet(ModelViewSet):
    serializer_class = TweetSerializer
    queryset = Tweet.objects.all()


class LikeViewSet(ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
