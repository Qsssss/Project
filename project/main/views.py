from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from main.models import Hotel, Room


def hotel_list(request):
    if request.method=='GET':
        hotels= Hotel.objects.all()

    hotels_json = [hotel.to_json() for hotel in hotels]
    data = {
        'hotels': hotels_json,
    }
    return JsonResponse(data)



def hotel_detail(request, hotel_id):
    try:
        hotel = Hotel.objects.get(id=hotel_id).to_json()

    except Hotel.DoesNotExist as e:
        return JsonResponse({'error':str(e)})
    return JsonResponse(hotel)


def room_list(request):
    rooms = Room.objects.all()
    rooms_json = [room.to_json() for room in rooms]
    return JsonResponse(rooms_json, safe=False)


def room_detail(request, room_id):
    try:
        room = Room.objects.get(id=room_id).to_json()

    except Room.DoesNotExist as e:
        return JsonResponse({'error':str(e)})

    return JsonResponse(room)

