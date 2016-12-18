from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinValueValidator
from decimal import Decimal


class Tour(models.Model):
    title = models.CharField(max_length=250, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    begin_date = models.DateField(verbose_name='Date of the beginning')
    end_date = models.DateField(verbose_name='Date of the ending')
    cost = models.DecimalField(verbose_name='Cost', decimal_places=2, max_digits=10,
                               validators=[MinValueValidator(Decimal('0.01')),])
    contact_details = models.CharField(max_length=200, verbose_name='Contact details')
    reservations = models.ManyToManyField(User, through='Reservation', related_name='reservations', blank=True)

    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'
        ordering = ('begin_date', 'cost',)

    def __str__(self):
        return self.title


class Place(models.Model):
    tour = models.ForeignKey(Tour, verbose_name='Tour', related_name='place_tour')
    latitude = models.FloatField(verbose_name='Latitude')
    longitude = models.FloatField(verbose_name='Longitude')
    address = models.CharField(max_length=150, verbose_name='Description')

    class Meta:
        verbose_name = 'Place'
        verbose_name_plural = 'Places'

    def __str__(self):
        return self.address


class Reservation(models.Model):
    user = models.ForeignKey(User, verbose_name='User', related_name='reservation_user')
    tour = models.ForeignKey(Tour, verbose_name='Tour', related_name='reservation_tour')
    addition_date = models.DateField(verbose_name='Date of addition', auto_now=True)
    paid_for = models.BooleanField(verbose_name='Paid for tour')

    class Meta:
        verbose_name = 'Reservation'
        verbose_name_plural = 'Reservations'
        ordering = ('addition_date',)

    def __str__(self):
        return 'User {0}, tour {1}'.format(self.user, self.tour)


class Rating(models.Model):
    tour = models.ForeignKey(Tour, verbose_name='Tour', related_name='rating_tour')
    average_rating = models.DecimalField(verbose_name='Average rating',
                                         decimal_places=2, max_digits=3)
    rating_count = models.IntegerField(verbose_name='Count of ratings')

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        ordering = ('average_rating',)

    def __str__(self):
        return self.average_rating


class Image(models.Model):
    tour = models.ForeignKey(Tour, verbose_name='Tour', related_name='image_tour')
    image = models.URLField(verbose_name='Image')
    description = models.CharField(max_length=300, verbose_name='Description')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ('description',)

    def __str__(self):
        return self.description
