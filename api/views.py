from rest_framework import serializers, viewsets
from django.apps import apps
from .serializers import UserSerializer, RoomsSerializer, BookingSerializer, ManagerSerializer
Booking = apps.get_model('booking', 'Booking')
User = apps.get_model('accounts', 'Customer')
Manager = apps.get_model('accounts', 'Manager')
Rooms = apps.get_model('booking', 'Rooms')


class CustomerViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class ManagerViewset(viewsets.ModelViewSet):
    queryset = Manager.objects.all()
    serializer_class = ManagerSerializer


class RoomsViewset(viewsets.ModelViewSet):
    queryset = Rooms.objects.all()
    serializer_class = RoomsSerializer


class BookingViewset(viewsets.ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer