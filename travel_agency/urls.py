from django.conf.urls import url, include
from rest_framework import routers
from travel_agency.travel_agency_api import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tours', views.TourViewSet)
router.register(r'reservations', views.ReservationViewSet)
router.register(r'comments', views.CommentViewSet)
router.register(r'ratings', views.RatingViewSet)
router.register(r'images', views.ImageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
