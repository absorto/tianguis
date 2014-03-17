from django.conf.urls import patterns, url

from vendimia.views import *

urlpatterns = patterns(
    '',
    url(r'^(\d)/ordenes/nueva/', orden_nueva),
    url(r'^(?P<vendimia_id>\d)/ordenes/(?P<orden_id>\d)/', get_orden),
    url(r'^(?P<vendimia_id>\d)/ordenes/', orden_index),



)
