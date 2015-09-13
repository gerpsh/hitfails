from django.conf.urls import include, url
from django.contrib import admin
from django.views.generic import RedirectView

urlpatterns = [
    url(r'^$', RedirectView.as_view(url='/posts/')),
	url(r'^admin/', include(admin.site.urls)),
	url(r'^posts/', include('posts.urls')),
	url(r'^site-auth/', include('site-auth.urls')),
]

handler404 = 'posts.views.resource_not_found'
handler500 = 'posts.views.server_error'
