from django.conf.urls import patterns, url

from vendimia.views import *

urlpatterns = patterns(
    '',
    url(r'^(?P<vendimia_id>\d)/pedidos/', pedidos_vendimia),
)
