from django.conf.urls.defaults import *
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.conf import settings

admin.autodiscover()

urlpatterns = i18n_patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^avatar/', include('avatar.urls')),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls')),
#    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^', include('cms.urls')),
)


#from cms.sitemaps import CMSSitemap
#from cmsplugin_blog.sitemaps import BlogSitemap

#urlpatterns = patterns('',
#    url(r'^sitemap.xml$', 'django.contrib.sitemaps.views.sitemap', {
#        'sitemaps': {
#            'cmspages': CMSSitemap,
#            'blogentries': BlogSitemap
#        }
#    }),
#    url(r'^', include('cms.urls'))
#)

if settings.DEBUG:
    urlpatterns = patterns('',
    url(r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),
) + urlpatterns
