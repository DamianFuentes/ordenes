from django.conf.urls import url
from .views import ordenes_detail, ordenes_list


urlpatterns = [
    url(r'^ordenes/$', ordenes_list),
    url(r'^ordenes/(?P<pk>[0-9]+)/$', ordenes_detail),
]