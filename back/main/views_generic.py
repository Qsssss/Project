from rest_framework.generics import UpdateAPIView
from rest_framework.permissions import IsAuthenticated
from main.models import Hotel
from rest_framework import generics
from main.serializers import HotelListSerializer2


class HotelListAPIView1(generics.ListCreateAPIView):
    queryset = Hotel.objects.all()
    serializer_class = HotelListSerializer2
    permission_classes = (IsAuthenticated, )
