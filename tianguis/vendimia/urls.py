from django.conf.urls import patterns, url

from vendimia.views import *

urlpatterns = patterns(
    '',

    url(r'^(?P<vendimia_id>\d)/ordenes/(?P<orden_id>\d)/', get_orden),
    url(r'^(?P<vendimia_id>\d)/', orden_nueva),



)
