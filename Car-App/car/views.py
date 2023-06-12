from rest_framework.viewsets import ModelViewSet
from .serializers import (
    Customer, CustomerSerializer,
    Car, CarSerializer,
    Reservation, ReservationSerializer
)

class FixView(ModelViewSet):
    pass


# -----------------------------------------------------------
# --------------------- CustomerView -----------------------
# -----------------------------------------------------------
class CustomerView(FixView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

# -----------------------------------------------------------
# --------------------- CarView --------------------------
# -----------------------------------------------------------
from rest_framework.permissions import IsAuthenticatedOrReadOnly
class CarView(FixView):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

# -----------------------------------------------------------
# --------------------- ReservationView ---------------------
# -----------------------------------------------------------
class ReservationView(FixView):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer