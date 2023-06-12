from rest_framework import serializers
from .models import (
    Car,
    Reservation,
    Customer
)

# -----------------------------------------------------------
# --------------------- FixSerializer -----------------------
# -----------------------------------------------------------
class FixSerializer(serializers.ModelSerializer):

    created = serializers.StringRelatedField()
    created_id = serializers.IntegerField(required=False)

    def create(self, validated_data):
        validated_data['created_id'] = self.context['request'].user.id
        return super().create(validated_data)
    

# -----------------------------------------------------------
# --------------------- CustomerSerializer -----------------
# -----------------------------------------------------------
class CustomerSerializer(FixSerializer):


    class Meta:
        model = Customer
        exclude = []

    def get_gender_text(self, obj):
        return obj.get_gender_display()


# -----------------------------------------------------------
# --------------------- FlightSerializer --------------------
# -----------------------------------------------------------
class CarSerializer(FixSerializer):

    # departure_text = serializers.SerializerMethodField() # return from get_field_name()
    # arrival_text = serializers.SerializerMethodField()

    class Meta:
        model = Car
        fields = (
            "id",
            "created",
            "created_id",
            "brand",
            "model",
            "plate_number",
            "gear",
            "rent_per_day",
            "availability",
        )

# -----------------------------------------------------------
# --------------------- ReservationSerializer ---------------
# -----------------------------------------------------------
class ReservationSerializer(FixSerializer):
    
    flight_id = serializers.IntegerField(write_only=True)
    passenger_ids = serializers.ListField(write_only=True)

    car = CarSerializer(read_only=True) # ForeingKey()
    customer = CustomerSerializer(read_only=True, many=True) # ManyToMany()

    class Meta:
        model = Reservation
        exclude = []

    def create(self, validated_data):
        validated_data["passenger"] = validated_data.pop('passenger_ids')
        return super().create(validated_data)