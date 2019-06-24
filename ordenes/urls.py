from django.conf.urls import url
from .views import orden_detail, ordenes_list, orden_foto


urlpatterns = [
    url(r'^ordenes/$', ordenes_list),
    url(r'^orden/(?P<pk>[0-9]+)/$', orden_detail),
    url(r'^orden_foto/(?P<pk>[0-9]+)/$', orden_foto),
]