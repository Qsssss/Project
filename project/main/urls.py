from django.urls import path
from main.views_fbv import hotel_list, hotel_detail, room_detail, room_list, hotel_rooms

urlpatterns = [
    path('hotels/', hotel_list),
    path('hotels/<int:id>/', hotel_detail),
    path('rooms/', room_list),
    path('rooms/<int:id>/', room_detail),
    path('hotel/<int:id>/rooms/', hotel_rooms)
]
