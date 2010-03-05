from django.conf.urls.defaults import *


urlpatterns = patterns('osm.views',
    url(r'^$', 'relay', name="osm_relay"),
)
