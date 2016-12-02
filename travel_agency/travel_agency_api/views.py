from rest_framework import viewsets

from django.contrib.auth.models import User
from travel_agency.travel_agency_api.models import Tour, Reservation, Comment, Rating, Image
from travel_agency.travel_agency_api.serializers import UserSerializer, TourSerializer, ReservationSerializer, \
    CommentSerializer, RatingSerializer, ImageSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from travel_agency.travel_agency_api.permissions import IsOwnerOrReadOnly


class UserViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing User objects """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class TourViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Tour objects """
    queryset = Tour.objects.all()
    serializer_class = TourSerializer
    permission_classes = (IsAdminUser, )


class ReservationViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Reservation objects """
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class CommentViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Comment objects """
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly)


class RatingViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Rating objects """
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer


class ImageViewSet(viewsets.ModelViewSet):
    """ ViewSet for viewing and editing Image objects """
    queryset = Image.objects.all()
    serializer_class = ImageSerializer
