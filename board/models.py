from django.db import models

# Create your models here.
class Master(models.Model):
	master_name = models.CharField(max_length=30)
	registration_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.master_name
		

class  Customer(models.Model):
	master = models.ForeignKey(Master, on_delete=models.CASCADE)
	customer_name = models.CharField(max_length=30)
	registration_date = models.DateTimeField(auto_now_add=True)
	waiting_status = models.BooleanField(default=True)
	email = models.EmailField(default=None)
	comment = models.CharField(max_length=2000, default=None,  blank=True)

	def __str__(self):
		return self.customer_name

	@property
	def is_waiting(self):
		return bool(self.waiting_status)
		