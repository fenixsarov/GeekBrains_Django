from django.conf.urls import url, include
from .views import *

urlpatterns = [
    url(r'^$', admin_page),
    url(r'^delete/user/(\d+)$', delete_user),
    url(r'^get_user_form/(\d+)/$', get_user_form),
    url(r'^create/user/(\d+)$', create_user),
    url(r'units/', admin_units, name='admin_units'),
    url(r'^create/$', admin_units_create, name='units_create'),
    url(r'^delete/(\d+)$', admin_units_delete, name='units_delete'),
    url(r'^update/(\d+)$', admin_units_update, name='units_update'),
    url(r'^detail/(\d+)$', admin_units_detail, name='units_detail')
]