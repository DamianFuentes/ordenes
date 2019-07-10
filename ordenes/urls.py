from django.conf.urls import url
from .views import orden_papel_detail,orden_papel_foto,orden_sistema_detail,ordenes_sistema_list,ordenes_papel_list,chequeo_credenciales
from django.conf.urls import url, include


urlpatterns = [
    url(r'^ordenes_papel/$', ordenes_papel_list),
    url(r'^orden_papel/(?P<entry>[A-Z]+-+[0-9]+)/$', orden_papel_detail),
    url(r'^orden_papel_foto/(?P<entry>[A-Z]+-+[0-9]+)/$', orden_papel_foto),
    url(r'^ordenes_sistema/$', ordenes_sistema_list),
    url(r'^orden_sistema/(?P<entry>[A-Z]+-+[0-9]+)/$', orden_sistema_detail),
    url(r'^chequeo_credenciales/$', chequeo_credenciales),
]