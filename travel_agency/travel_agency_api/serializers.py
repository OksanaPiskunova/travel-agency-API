from django.contrib.auth.models import User
from travel_agency.travel_agency_api.models import Tour, Place, Reservation, Rating, Image
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    """ Serializer to represent User model """
    class Meta:
        model = User
        fields = ('id', 'first_name', 'last_name', 'username', 'email', 'password')
        write_only_fields = ('password', )

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )
        user.set_password(validated_data['password'])
        user.save()

        return user


class PlaceSerializer(serializers.ModelSerializer):
    """ Serializer to represent Place model """
    class Meta:
        model = Place
        fields = ('id', 'tour', 'latitude', 'longitude', 'address')
        read_only_fields = ('id', )


class RatingSerializer(serializers.ModelSerializer):
    """ Serializer to represent Rating model """
    class Meta:
        model = Rating
        fields = ('id', 'tour', 'average_rating', 'rating_count')
        read_only_fields = ('id', 'rating_count')

    def update(self, instance, validated_data):
        sum_of_ratings = instance.average_rating * instance.rating_count
        instance.rating_count += 1
        instance.average_rating = (sum_of_ratings + validated_data['average_rating'] ) / \
                                  instance.rating_count
        instance.save()

        return instance


class ImageSerializer(serializers.ModelSerializer):
    """ Serializer to represent Image model """
    class Meta:
        model = Image
        fields = ('id', 'tour', 'image', 'description')
        read_only_fields = ('id', )



class TourSerializer(serializers.ModelSerializer):
    """ Serializer to represent Tour model """
    image_tour = ImageSerializer(many=True, read_only=True)
    rating_tour = RatingSerializer(many=True, read_only=True)
    place_tour = PlaceSerializer(many=True, read_only=True)

    class Meta:
        model = Tour
        fields = ('id', 'title', 'content', 'begin_date', 'end_date', 'cost', 'contact_details',
                  'image_tour', 'rating_tour', 'place_tour')


class ReservationSerializer(serializers.ModelSerializer):
    """ Serializer to represent Reservation model """
    #tour = TourSerializer(many=True, read_only=True)

    class Meta:
        model = Reservation
        fields = ('user', 'tour', 'addition_date', 'paid_for')
        read_only_fields = ('addition_date', )
