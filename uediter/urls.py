import os
from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
from uediter import settings
from uediter.settings import STATIC_URL

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'uediter.views.home', name='home'),
    # url(r'^uediter/', include('uediter.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^edit$', 'app.web.views.edit'),
    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^ueditor_config/$', 'app.Ueditor.views.customConfig'),
)

urlpatterns += patterns('',
                        (r'^assets/(.*)$', 'django.views.static.serve',
                         {'document_root': os.path.join(settings.SRC_ROOT[0], 'amaze')}),
                        (r'^img/(.*)$', 'django.views.static.serve',
                         {'document_root': os.path.join(settings.SRC_ROOT[0], 'img')}),
                        (r'^js/(.*)$', 'django.views.static.serve',
                         {'document_root': os.path.join(settings.SRC_ROOT[0], 'js')}),
                        (r'^css/(.*)$', 'django.views.static.serve',
                         {'document_root': os.path.join(settings.SRC_ROOT[0], 'css')}),
                        (r'^ueditor/(.*)$', 'django.views.static.serve',
                         {'document_root': os.path.join(settings.SRC_ROOT[0], 'ueditor')}),
                        (r'^static/(.*)$', 'django.views.static.serve', {'document_root': settings.STATICFILES_DIRS}),
)