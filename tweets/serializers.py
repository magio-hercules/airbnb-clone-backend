from rest_framework import serializers
from .models import Tweet, Like
from users.serializers import TinyUserSerializer


class TweetDetailSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = (
            "pk",
            "payload",
            "user",
        )


class TweetListSerializer(serializers.ModelSerializer):

    user = TinyUserSerializer(read_only=True)

    class Meta:
        model = Tweet
        fields = (
            "pk",
            "user",
            "payload",
        )


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"
