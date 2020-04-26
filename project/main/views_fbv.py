from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import Hotel, Room
from main.serializers import HotelListSerializer, RoomListSerializer


@api_view(['GET', 'POST'])
def hotel_list(request):
    if request.method == 'GET':
        hotels = Hotel.objects.all()
        serializer = HotelListSerializer(hotels, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = HotelListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def hotel_detail(request, id):
    try:
        hotel = Hotel.objects.get(id=id)
    except Hotel.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = HotelListSerializer(hotel)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = HotelListSerializer(instance=hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        hotel.delete()
        return Response({'deleted': True})


@api_view(['GET', 'POST'])
def room_list(request):
    if request.method == 'GET':
        rooms = Room.objects.all()
        serializer = RoomListSerializer(rooms, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = RoomListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def room_detail(request, id):
    try:
        room = Room.objects.get(id=id)
    except Room.DoesNotExist as e:
        return Response({'error': str(e)})

    if request.method == 'GET':
        serializer = RoomListSerializer(room)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = RoomListSerializer(instance=room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    elif request.method == 'DELETE':
        room.delete()
        return Response({'deleted': True})


@api_view(['GET'])
def hotel_rooms(request, id):
    if request.method == 'GET':
        try:
            hotel = Hotel.objects.get(id=id)
        except Hotel.DoesNotExist as e:
            return Response({'error': str(e)})
        rooms = Room.objects.filter(hotel=hotel)
        serializer = RoomListSerializer(rooms, many=True)
        return Response(serializer.data)
