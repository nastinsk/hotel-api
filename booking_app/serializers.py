from rest_framework import serializers

from .models import Reservation

class ReservationSerializer(serializers.ModelSerializer):
  class Meta:
    model = Reservation
    fields = [
      'id', 'customer_name', 'room_name', 'check_in_date', 'check_out_date', 'booking_created_date', 'booking_updated_date', 'special_accomodations', 'staff_member_name'
      ]
   