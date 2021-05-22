from django.urls import path, include
from django.views.generic import TemplateView
from . import views

urlpatterns = [

	path('', views.showservice, name='showservice'),
	path('<int:service_id>/', views.specific_service, name='specific_service'),
	path('profile/', views.ProfileUpdate.as_view(), name='profile_url'),
	path('booking/', views.ServiceBookingAdd.as_view(), name='booking_url'),
	path('orders/', views.UserOrdersView.as_view(), name='orders_url'),
	]