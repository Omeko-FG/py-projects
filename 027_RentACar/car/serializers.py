from rest_framework import serializers

from .models import (
    Car,
    Reservation
)


# ---------------------------------
# FixSerializer
# ---------------------------------
class FixSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(required=False, read_only=True)

    def create(self, validated_data):
        validated_data['user_id'] = self.context['request'].user.id
        return super().create(validated_data)

# ---------------------------------
# CarSerializer
# ---------------------------------
class CarSerializer(FixSerializer):
    car = serializers.StringRelatedField()
    car_id = serializers.IntegerField()
    class Meta:
        model = Car
        exclude = []


# ---------------------------------
# ReservationSerializer
# ---------------------------------
class ReservationSerializer(FixSerializer):

    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField(required=False, read_only=True)
    class Meta:
        model = Reservation
        exclude = []