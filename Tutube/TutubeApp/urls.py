from django.conf.urls import patterns, url
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView
from views import HomePageView, CanalListView, AuthorListView, VideoListView

urlpatterns = [
    url(r'^$', HomePageView.as_view()),
    url(r'^canal/$', CanalListView.as_view(), name = 'canal-list',),
    url(r'^author/$', AuthorListView.as_view(), name = 'author-list',),
    url(r'^video/$', VideoListView.as_view(), name = 'video-list',),
    url(r'^canal.json$', 'TutubeApp.views.CanalJson'),
    url(r'^author.json$', 'TutubeApp.views.AuthorJson'),
    url(r'^video.json$', 'TutubeApp.views.VideoJson'),
    url(r'^canal.xml$', 'TutubeApp.views.CanalXml'),
    url(r'^author.xml$', 'TutubeApp.views.AuthorXml'),
    url(r'^video.xml$', 'TutubeApp.views.VideoXml'),
]
