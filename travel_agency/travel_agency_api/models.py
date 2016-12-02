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
    comments = models.ManyToManyField(User, through='Comment', related_name='comments', blank=True)

    class Meta:
        verbose_name = 'Tour'
        verbose_name_plural = 'Tours'
        ordering = ('begin_date', 'cost',)

    def __str__(self):
        return self.title


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


class Comment(models.Model):
    user = models.ForeignKey(User, verbose_name='User', related_name='comment_user')
    tour = models.ForeignKey(Tour, verbose_name='Tour', related_name='comment_tour')
    title = models.CharField(max_length=150, verbose_name='Title')
    content = models.TextField(verbose_name='Content')
    addition_date = models.DateTimeField(verbose_name='Time of addition')

    class Meta:
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'
        ordering = ('title',)

    def __str__(self):
        return 'Comment {0} by user {1}'.format(self.title, self.user)


class Rating(models.Model):
    tour = models.ForeignKey(Tour, verbose_name='Tour')
    average_rating = models.DecimalField(verbose_name='Average rating', decimal_places=2, max_digits=3)
    rating_count = models.IntegerField(verbose_name='Count of ratings')

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'
        ordering = ('average_rating',)

    def __str__(self):
        return self.average_rating


class Image(models.Model):
    tour = models.ForeignKey(Tour, verbose_name='Tour')
    image = models.ImageField(verbose_name='Image')
    description = models.CharField(max_length=300, verbose_name='Description')

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
        ordering = ('description',)

    def __str__(self):
        return self.description
