from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^user/(?P<user>[a-zA-Z0-9]+)/$', views.user_view, name='user_view'),
	url(r'^(?P<post_id>[0-9]+)/$', views.post_view, name='post_view'),
	url(r'^tag/(?P<tag_name>[a-zA-Z0-9]+)/$', views.tag_view, name='tag_view'),
	url(r'^add-post/', views.post_form, name='post_form'),
	url(r'^formatting-help/', views.formatting_help, name='formatting_help'),
	url(r'^add-comment/(?P<post_id>[0-9]+)/$', views.add_parent_comment, name='add_parent_comment'),
	url(r'^add-mark/(?P<post_id>[0-9]+)/$', views.add_mark, name='add_mark'),
	url(r'^remove-mark/(?P<post_id>[0-9]+)/$', views.remove_mark, name='remove_mark'),
	url(r'^search/', include('haystack.urls')),
]
