from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from maps.views import view_map

# all urls begin with http://localhost:8000/map/
urlpatterns = [
    #  ex valid call from to  /api/directions/1587848.414,5879564.080,2&1588005.547,5879736.039,2
    # url(r'^(?P<map_name>[0-9a-zA-Z_-]+)/$', 'view_map', name='map_name'),
    url(r'^(?P<map_name>[^/]+)/$', view_map, name='map_name'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
