from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'password': self.password
        }


class Hotel(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(default='')
    telephone_number = models.IntegerField()
    city = models.CharField(max_length=100)
    comments = models.TextField(default='')
    image = models.TextField(default='')
    number_of_rooms = models.IntegerField()
    stars = models.IntegerField()

    def to_json(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'telephone number': self.telephone_number,
            'city': self.city,
            'comments': self.comments,
            'image': self.image,
            'number of rooms': self.number_of_rooms,
            'stars': self.stars
        }


class Room(models.Model):
    photo = models.TextField()
    description = models.TextField()
    price = models.FloatField()
    people = models.IntegerField()
    saved = models.BooleanField(default=True)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE, default=1)

    def to_json(self):
        return {
            'photo': self.photo,
            'description': self.description,
            'price': self.price,
            'people': self.people,
            'saved': self.saved
        }


class Saved(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    def to_json(self):
        return {
            'status': self.status
        }


class LuxHotels(models.Manager):
    def get_query_set(self):
        return super(LuxHotels, self).get_queryset().filter(stars=5)
