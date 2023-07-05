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

    class Meta:
        model = Car
        exclude = []


# ---------------------------------
# ReservationSerializer
# ---------------------------------
class ReservationSerializer(FixSerializer):
    car = serializers.StringRelatedField()
    car_id = serializers.IntegerField()

    total_price = serializers.SerializerMethodField()
    class Meta:
        model = Reservation
        exclude = []


    def get_total_price(self, obj):
        return obj.car.rent_per_day * (obj.end_date - obj.start_date).days