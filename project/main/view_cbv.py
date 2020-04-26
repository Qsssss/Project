from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from main.models import Hotel, Room
from main.serializers import HotelListSerializer, RoomListSerializer


class HotelListAPIView(APIView):
    def get(self, request):
        hotels = Hotel.objects.all()
        serializer = HotelListSerializer(hotels, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = HotelListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class HotelDetailAPIView(APIView):
    def get_hotel(self, id):
        try:
            return Hotel.objects.get(id=id)
        except Hotel.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, id):
        hotel = self.get_hotel(id)
        serializer = HotelListSerializer(hotel)
        return Response(serializer.data)

    def put(self, request, id):
        hotel = self.get_hotel(id)
        serializer = HotelListSerializer(instance=hotel, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, id):
        hotel = self.get_hotel(id)
        hotel.delete()
        return Response({'deleted': True})


class RoomListAPIView(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomListSerializer(rooms, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = RoomListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response({'error': serializer.errors},
                        status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RoomDetailAPIView(APIView):
    def get_room(self, id):
        try:
            return Room.objects.get(id=id)
        except Hotel.DoesNotExist as e:
            return Response({'error': str(e)})

    def get(self, request, id):
        room = self.get_room(id)
        serializer = RoomListSerializer(room)
        return Response(serializer.data)

    def put(self, request, id):
        room = self.get_room(id)
        serializer = RoomListSerializer(instance=room, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response({'error': serializer.errors})

    def delete(self, request, id):
        room = self.get_room(id)
        room.delete()
        return Response({'deleted': True})
