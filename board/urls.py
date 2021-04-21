from django.urls import path, include
from . import views

app_name = "board"
urlpatterns = [	
	path('', views.IndexView.as_view(), name='index'),
	path('master/<int:pk>/', views.MasterDetailView.as_view(), name='master_detail'),
	path('customer/<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
	path('customer/<int:pk>/edit', views.CustomerUpdateView.as_view(), name='customer_update'),
	path('customer/create', views.CustomerCreateView.as_view(), name='customer_create'),
	path('customer/<int:pk>/delete', views.CustomerDeleteView.as_view(), name='customer_delete'),	
]