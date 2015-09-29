from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.index, name='index'),
	url(r'^(?P<post_id>[0-9]+)/$', views.post_view, name='post_view'),
	url(r'^tag/(?P<tag_name>.+)/$', views.tag_view, name='tag_view'),
	url(r'^add-post/', views.post_form, name='post_form'),
	url(r'^formatting-help/', views.formatting_help, name='formatting_help'),
	url(r'^add-comment/(?P<post_id>[0-9]+)/$', views.add_parent_comment, name='add_parent_comment'),
	url(r'^search/', include('haystack.urls')),
]
