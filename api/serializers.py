from rest_framework import serializers
from django.apps import apps
Booking = apps.get_model('booking', 'Booking')
User = apps.get_model('accounts', 'Customer')
Manager = apps.get_model('accounts', 'Manager')
Rooms = apps.get_model('booking', 'Rooms')


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'email',
            'image'
        ]


class ManagerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manager
        fields = [
            'id',
            'username',
            'password',
            'email',
            'image'
        ]


class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = [
            'id',
            'manager',
            'room_no',
            'room_type',
            'is_available',
            'price',
            'no_of_days_advance',
            'start_date',
            'image'
        ]


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = [
            'id',
            'room_no',
            'user_id',
            'start_day',
            'end_day',
            'amount',
            'booked_on'
        ]