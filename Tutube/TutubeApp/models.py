from __future__ import unicode_literals
from django.db import models
from datetime import date
#from django.contrib.auth.models import User
#from django.core.urlresolvers import reverse
# Create your models here.
class Canal(models.Model):
    nom_canal = models.TextField()
    URL_canal = models.URLField(blank=True, null=False)
    data_crea = models.DateField(default=date.today)

    def __unicode__(self):
        return self.nom_canal


class Author(models.Model):
    nom_autor = models.TextField(blank=False, null=True)
    edat_autor = models.IntegerField(blank=True, null=True)

    def __unicode__(self):
        return self.nom_autor

class Video(models.Model):
    titol_video = models.TextField(blank=False, null=False)
    url_video = models.URLField(blank = False, null = False)
    longitud_video = models.IntegerField(blank=True, null=True)
    data_up = models.DateField(blank=True, null=True)

    def __unicode__(self):
        return  self.titol_video
