from django.urls import path, include
from django.views.generic import TemplateView
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [

	path('', views.showblog, name='showblog'),
	path('<int:post_id>/', views.specific_post, name='specific_post'),
	# path("register", views.register, name="register"),
	path('register/', TemplateView.as_view(template_name="account/base.html")),
    path('accounts/', include('allauth.urls')),
    path("logout/", LogoutView.as_view(), name="logout"),
    path('social-auth/', include('social_django.urls', namespace="social")),
    # path('logout', LogoutView.as_view()), где логинишься
]