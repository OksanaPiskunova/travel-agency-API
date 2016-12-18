from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend

from django.contrib.auth.models import User
from travel_agency.travel_agency_api.models import Tour, Place, Reservation, Rating, Image
from travel_agency.travel_agency_api.serializers import UserSerializer, TourSerializer, PlaceSerializer, \
    ReservationSerializer, RatingSerializer, ImageSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from travel_agency.travel_agency_api.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing User objects """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'username')


class TourViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Tour objects """
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'title', 'begin_date', 'end_date', 'cost')


class PlaceViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Place objects """
    queryset = Place.objects.all()
    serializer_class = PlaceSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'tour', 'latitude', 'longitude', 'address')


class ReservationViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Reservation objects """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'user', 'tour', 'addition_date')


class RatingViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Rating objects """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'tour', 'average_rating')


class ImageViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Image objects """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
    filter_backends = (DjangoFilterBackend,)
    filter_fields = ('id', 'tour')
