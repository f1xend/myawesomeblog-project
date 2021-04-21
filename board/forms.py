from django import forms
from .models import Master, Customer

class MasterForm(forms.ModelForm):
	class Meta:
		model = Master
		fields = "__all__"


class CustomerForm(forms.ModelForm):
	class Meta:
		model = Customer
		fields = "__all__"