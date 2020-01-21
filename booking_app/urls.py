from django.urls import path
from .views import ReservationsList, ReservationDetail

urlpatterns = [
  path('reservations/', ReservationsList.as_view(), name='reservations_list')
  path('posts/<int:pk>/', ReservationDetail.as_view(), name='post_list'),
]