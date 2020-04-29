from django.urls import path
from main.views_fbv import hotel_list, hotel_detail, room_detail, room_list, hotel_rooms, saved_rooms
from main.view_cbv import NewUsersAPIView, HotelList, HotelListAPIView
from rest_framework_jwt.views import obtain_jwt_token
from main.views_generic import HotelListAPIView1

urlpatterns = [
    path('login/', obtain_jwt_token),
    path('hotels/', HotelListAPIView.as_view()),
    path('hotelss/', HotelListAPIView1.as_view()),
    path('hotels/<int:id>/', hotel_detail),
    path('rooms/', room_list),
    path('rooms/<int:id>/', room_detail),
    path('hotel/<int:id>/rooms/', hotel_rooms),
    path('users/', NewUsersAPIView.as_view()),
    path('saved/', saved_rooms)
]
