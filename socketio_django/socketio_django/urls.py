from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from socketio import sdjango

sdjango.autodiscover()

urlpatterns = patterns('',
                       url(r'^', include('heart_beat.urls')),
                       url(r'^socket\.io', include(sdjango.urls)),
)


urlpatterns += staticfiles_urlpatterns()

if settings.DEBUG:
    # static files (images, css, javascript, etc.)
    urlpatterns += patterns(
        '',
        (r'^media/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT}))