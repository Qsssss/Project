from rest_framework import serializers
from main.models import Hotel, Room


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
    hotel = serializers.ReadOnlyField(source='hotel.id')

    class Meta:
        model = Room
        fields = "__all__"
