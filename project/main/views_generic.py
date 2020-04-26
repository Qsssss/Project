from typing import Type, List

from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from main.models import Hotel
from main.serializers import HotelListSerializer

class HotelListAPIView(UpdateAPIView):
    hotel = Hotel.objects.all()
    serializer_class = HotelListSerializer
    permission_classes = [IsAuthenticated,]