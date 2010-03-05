import os
import sys
import site

site.addsitedir('/home/taylan/sites/osm-relay/lib/python2.5/site-packages')

sys.path.append("/home/taylan/sites/osm-relay/src/osm-relay/web")
sys.path.append("/home/taylan/sites/osm-relay/src/osm-relay/web/osm_relay")

os.environ["DJANGO_SETTINGS_MODULE"] = "osm_relay.settings"

import django.core.handlers.wsgi

application = django.core.handlers.wsgi.WSGIHandler()
