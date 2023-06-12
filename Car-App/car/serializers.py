from rest_framework import serializers
from .models import (
    Car,
    Reservation
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