from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from vendimia import urls as vendimia_urls
from vendimia.views import pedidos_vendimia, pedido_vendimia_user, gran_pedido

urlpatterns = patterns('',

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^admin/vendimia/vendimia/(?P<vendimia_id>\d)/gran_pedido/', gran_pedido),
    url(r'^admin/vendimia/vendimia/(?P<vendimia_id>\d)/pedidos/(?P<user_id>\d)/', pedido_vendimia_user),
    url(r'^admin/vendimia/vendimia/(?P<vendimia_id>\d)/pedidos/', pedidos_vendimia),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^vendimia/', include(vendimia_urls)),
)
