from django.urls import path

# '/car/':
urlpatterns = [
]


from rest_framework.routers import DefaultRouter
from .views import (
    CustomerView,
    CarView,
    ReservationView
)
router = DefaultRouter()
router.register('customer', CustomerView)
router.register('car', CarView)
router.register('reservation', ReservationView)
urlpatterns += router.urls