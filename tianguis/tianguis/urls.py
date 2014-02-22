from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

from vendimia import urls as vendimia_urls

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tianguis.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^accounts/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^vendimia/', include(vendimia_urls)),
)
