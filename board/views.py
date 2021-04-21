from django.shortcuts import render, redirect, get_object_or_404
from .models import Master, Customer
# from .forms import MasterForm, CustomerForm

from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
# Create your views here.

class IndexView(ListView):
	template_name = "board/index.html"
	context_object_name = "customer_list"

	def get_queryset(self):
		return Customer.objects.filter(waiting_status=True)

class CustomerCreateView(CreateView):
	model = Customer
	fields = ["master","customer_name"]
	success_url = reverse_lazy("board:index")

class CustomerDetailView(DetailView):
	template_name = "board/customer_detail.html"
	model = Customer

class CustomerUpdateView(UpdateView):
	model = Customer
	fields = ["customer_name","email", "waiting_status"]
	template_name_suffix = "_update_form"
	success_url = reverse_lazy("board:index")

	def waiting_set(self):
		qs = super(CustomerUpdateView, self).get_queryset
		return qs.filter(owner=self.request.user)

class CustomerDeleteView(DeleteView):
	model = Customer
	success_url = reverse_lazy("board:index")

	# def get_queryset(self):
	# 	qs = super(CustomerDeleteView, self).get_queryset()
	# 	return qs.filter(owner=self.request.user)

	

class MasterDetailView(DetailView):
	template_name = "board/master_detail.html"
	model = Master
