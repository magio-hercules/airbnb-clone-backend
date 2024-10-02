from django.shortcuts import render
from django.http import HttpResponse
from .models import Room


def see_all_rooms(request):
    rooms = Room.objects.all()
    return render(
        request,
        "all_rooms.html",
        {
            "rooms": rooms,
            "title": "Hello this title comes from django!",
        },
    )


def see_one_room(request, room_pk):
    try:
        print(f"see_one_room room_pk: {room_pk}")
        room = Room.objects.get(pk=room_pk)
        print(room)
        return render(
            request,
            "room_detail.html",
            {
                "room": room,
            },
        )
    except Room.DoesNotExist:
        return render(
            request,
            "room_detail.html",
            {
                "not_found": True,
            },
        )
