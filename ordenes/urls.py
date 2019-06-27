from django.conf.urls import url
from .views import orden_papel_detail, ordenes_papel_list, orden_papel_foto, orden_sistema_detail, ordenes_sistema_list, orden_completa


urlpatterns = [
    url(r'^ordenes_papel/$', ordenes_papel_list),
    url(r'^orden_papel/(?P<entry>[A-Z]+-+[0-9]+)/$', orden_papel_detail),
    url(r'^orden_papel_foto/(?P<entry>[A-Z]+-+[0-9]+)/$', orden_papel_foto),
    url(r'^ordenes_sistema/$', ordenes_sistema_list),
    url(r'^orden_sistema/(?P<entry>[A-Z]+-+[0-9]+)/$', orden_sistema_detail),
    url(r'^orden_completa/(?P<entry>[A-Z]+-+[0-9]+)/$', orden_completa),
]