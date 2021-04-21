from django.db import models

# Create your models here.
class Booking(object):
	booking_title = models.CharField(max_length=300)
		
class Seat(object):
	seat_title = models.CharField(max_length=300)
		
class BookingSeat(object):
	bookingseat_title = models.CharField(max_length=300)
		