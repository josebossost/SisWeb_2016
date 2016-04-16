from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'Tutube.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^TutubeApp/',include('TutubeApp.urls',namespace='TutubeApp')),
    url(r'^accounts/login/$', login, name='login'),
    url(r'^accounts/logout/$', login, name='logout'),
)
