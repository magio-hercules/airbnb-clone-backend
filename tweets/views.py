from django.db import transaction
from rest_framework.viewsets import ModelViewSet
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.response import Response
from rest_framework.exceptions import (
    NotFound,
    ParseError,
    PermissionDenied,
)
from .models import Tweet, Like
from .serializers import TweetDetailSerializer, TweetListSerializer, LikeSerializer


class Tweets(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get(self, request):
        all_tweets = Tweet.objects.all()
        serializer = TweetListSerializer(
            all_tweets,
            many=True,
            context={"request": request},
        )
        return Response(serializer.data)

    def post(self, request):
        serializer = TweetDetailSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.save(
                user=request.user,
            )
            serializer = TweetDetailSerializer(room)
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


class TweetDetail(APIView):

    permission_classes = [IsAuthenticatedOrReadOnly]

    def get_object(self, pk):
        try:
            return Tweet.objects.get(pk=pk)
        except Tweet.DoesNotExist:
            raise NotFound

    def get(self, request, pk):
        tweet = self.get_object(pk)
        serializer = TweetDetailSerializer(
            tweet,
        )
        return Response(serializer.data)

    def put(self, request, pk):
        tweet = self.get_object(pk)
        if tweet.user != request.user:
            raise PermissionDenied
        serializer = TweetDetailSerializer(
            tweet,
            data=request.data,
            partial=True,
        )
        if serializer.is_valid():
            updated_data = serializer.save()
            return Response(
                TweetDetailSerializer(updated_data).data,
            )
        else:
            return Response(serializer.errors)

    def delete(self, request, pk):
        tweet = self.get_object(pk)
        if tweet.user != request.user:
            raise PermissionDenied
        tweet.delete()
        return Response(status=HTTP_204_NO_CONTENT)


class LikeViewSet(ModelViewSet):
    serializer_class = LikeSerializer
    queryset = Like.objects.all()
