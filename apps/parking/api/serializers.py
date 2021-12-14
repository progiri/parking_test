from rest_framework import serializers

from apps.parking.models import Space, SpaceBooking


class SpaceBookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = SpaceBooking
        fields = ('id', 'start_of_booking', 'end_of_booking')


class SpaceSerializer(serializers.ModelSerializer):
    bookings = SpaceBookingSerializer(many=True, required=False)

    class Meta:
        model = Space
        fields = ('id', 'number', 'bookings')
