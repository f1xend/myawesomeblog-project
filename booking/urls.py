from django.urls import path 
from . import views

urlpatterns = [
    path('', views.booking_seat_list, name='booking_seat_list'),
    path('booking_seat/<int:pk>/', views.booking_seat_detail, name='booking_seat_detail'),
    path('booking_seat/new/', views.booking_seat_new, name='booking_seat_new'),
]