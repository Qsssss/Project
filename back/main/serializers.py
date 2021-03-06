from rest_framework import serializers
from main.models import Hotel, Room, User


class UserSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    username = serializers.CharField()
    password = serializers.CharField()

    def create(self, validated_data):
        user = User(username=validated_data.get('username'), password=validated_data.get('password'))
        return user


class HotelListSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField()
    description = serializers.CharField()
    telephone_number = serializers.IntegerField()
    city = serializers.CharField()
    comments = serializers.CharField()
    image = serializers.CharField()
    number_of_rooms = serializers.IntegerField()
    stars = serializers.IntegerField()

    def create(self, validated_data):
        hotel = Hotel.objects.create(name=validated_data.get('name', 'default name'),
                                     description=validated_data.get('description', 'asdasdasd'),
                                     telephone_number=validated_data.get('telephone number', '87770007700'),
                                     city=validated_data.get('city'),
                                     comments=validated_data.get('comments', 'the best hotel'),
                                     image=validated_data.get('image'),
                                     number_of_rooms=validated_data.get('number of rooms', 1),
                                     stars=validated_data.get('stars'))
        return hotel

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', 'default name')
        instance.description = validated_data.get('description', 'asdasdasd')
        instance.telephone_number = validated_data.get('telephone number', '87770007700')
        instance.city = validated_data.get('city')
        instance.comments = validated_data.get('comments', 'the best hotel')
        instance.image = validated_data.get('image')
        instance.number_of_rooms = validated_data.get('number of rooms', 1)
        instance.stars = validated_data.get('stars')
        instance.save()
        return instance


class RoomListSerializer(serializers.ModelSerializer):
    hotel_id = serializers.IntegerField(write_only=True)

    class Meta:
        model = Room
        fields = "__all__"


class HotelListSerializer2(serializers.ModelSerializer):
    # name = serializers.CharField(max_length=200)

    class Meta:
        model = Hotel
        fields = ('id', 'name')

