from rest_framework.viewsets import ModelViewSet
from .models import ChattingRoom, Message
from .serializers import ChattingRoomSerializer, MessageSerializer


class ChattingRoomViewSet(ModelViewSet):
    serializer_class = ChattingRoomSerializer
    queryset = ChattingRoom.objects.all()


class MessageViewSet(ModelViewSet):
    serializer_class = MessageSerializer
    queryset = Message.objects.all()
