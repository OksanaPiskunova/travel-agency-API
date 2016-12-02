from django.contrib.auth.models import User
from travel_agency.travel_agency_api.models import Tour, Reservation, Comment, Rating, Image
from rest_framework import serializers


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer to represent User model """
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')


class TourSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer to represent Tour model """
    class Meta:
        model = Tour
        fields = ('title', 'content', 'begin_date', 'end_date', 'cost', 'contact_details')


class ReservationSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer to represent Reservation model """
    class Meta:
        model = Reservation
        fields = ('user', 'tour', 'addition_date', 'paid_for')
        read_only_fields = ('addition_date', )


class CommentSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer to represent Comment model """
    class Meta:
        model = Comment
        fields = ('user', 'tour', 'title', 'content')


class RatingSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer to represent Rating model """
    class Meta:
        model = Rating
        fields = ('average_rating', )
        read_only_fields = ('average_rating', )


class ImageSerializer(serializers.HyperlinkedModelSerializer):
    """ Serializer to represent Image model """
    class Meta:
        model = Image
        fields = ('tour', 'image', 'description')
