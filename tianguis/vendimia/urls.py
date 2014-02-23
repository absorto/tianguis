from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'adios/', 'vendimia.views.adios'),
    url(r'/', 'vendimia.views.hola'),

)
