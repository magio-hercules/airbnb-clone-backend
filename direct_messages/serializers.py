from rest_framework import serializers
from .models import ChattingRoom, Message


class ChattingRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChattingRoom
        fields = "__all__"


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = "__all__"
