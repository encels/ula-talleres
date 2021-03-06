from django.conf.urls.defaults import patterns, include, url
from django.conf import settings

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'eisula.views.home', name='home'),
    url(r'^eisula/', include('eisula.proyecto.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^m/(?P<path>.*)$',
                                'django.views.static.serve', {'document_root':
                                                              settings.MEDIA_ROOT,
                                                             }),
                           )
