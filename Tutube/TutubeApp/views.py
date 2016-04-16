from django.views.generic import TemplateView, ListView
from django.views.generic.base import TemplateResponseMixin
from django.http import HttpResponse
from django.core import serializers
from models import Canal, Author, Video

# Create your views here.

class HomePageView(TemplateView):
    template_name = "home_page.html"

# List Views
class CanalListView(ListView):
    model = Canal
    context_object_name = 'canal_list'
    template_name = 'canal_list.html'

class AuthorListView(ListView):
    model = Author
    context_object_name = 'author_list'
    template_name = 'author_list.html'

class VideoListView(ListView):
    model = Video
    context_object_name = 'video_list'
    template_name = 'video_list.html'


#JSON
def CanalJson(request):
    jsonList = Canal.objects.all()
    serializedJson = serializers.serialize(u"json", jsonList)
    return HttpResponse(serializedJson, content_type=u"application/json")

def AuthorJson(request):
    jsonList = Author.objects.all()
    serializedJson = serializers.serialize(u"json", jsonList)
    return HttpResponse(serializedJson, content_type=u"application/json")

def VideoJson(request):
    jsonList = Video.objects.all()
    serializedJson = serializers.serialize(u"json", jsonList)
    return HttpResponse(serializedJson, content_type=u"application/json")


#XML
def CanalXml(request):
    xmlList = Canal.objects.all()
    serializedXml = serializers.serialize(u"xml", xmlList)
    return HttpResponse(serializedXml, content_type=u"application/xml")

def AuthorXml(request):
    xmlList = Author.objects.all()
    serializedXml = serializers.serialize(u"xml", xmlList)
    return HttpResponse(serializedXml, content_type=u"application/xml")

def VideoXml(request):
    xmlList = Video.objects.all()
    serializedXml = serializers.serialize(u"xml", xmlList)
    return HttpResponse(serializedXml, content_type=u"application/xml")
