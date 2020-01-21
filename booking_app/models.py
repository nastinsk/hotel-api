from django.db import models
from django.contrib.auth.models import User


class Reservation(models.Model):
  customer_name = models.CharField(max_length=120)
  room_name = models.CharField(max_length=30)
  check_in_date = models.DateField()
  check_out_date = models.DateField()
  booking_created_date = models.DateTimeField(auto_now_add=True)
  booking_updated_date = models.DateTimeField(auto_now=True)
  special_accomodations = models.CharField(max_length=500)
  staff_member_name = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    return f"Reservation for {self.customer_name}"