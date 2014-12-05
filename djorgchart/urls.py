from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'orgchart.views.home', name='chart_home'),
    url(r'^chart/new/$', 'orgchart.views.chart_new', name='chart_new'),
    url(r'^chart/edit/(?P<id>[0-9]+)/$', 'orgchart.views.chart_edit', name='chart_edit'),
    url(r'^chart/delete/(?P<id>[0-9]+)/$', 'orgchart.views.chart_delete', name='chart_delete'),

    # url(r'^blog/', include('blog.urls')),

    # url(r'^admin/', include(admin.site.urls)),
)

# включение отдачи статики в режиме отладки
if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.STATIC_ROOT,
            }),
   )