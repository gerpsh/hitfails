from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^login/', views.login_view, name='login'),
	url(r'^logout/', views.logout_view, name='logout'),
	url(r'^register/', views.register_view, name='register'),
	url(r'^username-check/(?P<username>[a-zA-Z0-9_]+)/$', views.username_check, name='username_check'),
]