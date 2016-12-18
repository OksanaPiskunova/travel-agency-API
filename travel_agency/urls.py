from django.conf.urls import url, include
from rest_framework import routers
from travel_agency.travel_agency_api import views

from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'tours', views.TourViewSet)
router.register(r'places', views.PlaceViewSet)
router.register(r'reservations', views.ReservationViewSet)
router.register(r'ratings', views.RatingViewSet)
router.register(r'images', views.ImageViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^api-token-auth/', obtain_jwt_token),
    url(r'^api-token-refresh/', refresh_jwt_token),
    url(r'^api-token-verify/', verify_jwt_token),
]
