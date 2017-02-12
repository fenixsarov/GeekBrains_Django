from django.conf.urls import url
from .views import admin_page, admin_units, admin_units_create, admin_units_delete, admin_units_detail, \
    admin_units_update, delete_user, create_user, get_user_form

urlpatterns = [
    url(r'^$', admin_page),
    url(r'^delete/user/(\d+)$', delete_user),
    url(r'^get_user_form/(\d+)$', get_user_form),
    url(r'^create/user/(\d+)$', create_user),
    url(r'units/', admin_units, name='admin_units'),
    url(r'^create/units$', admin_units_create, name='units_create'),
    url(r'^delete/units/(\d+)$', admin_units_delete, name='units_delete'),
    url(r'^update/units/(\d+)$', admin_units_update, name='units_update'),
    url(r'^detail/units/(\d+)$', admin_units_detail, name='units_detail')
]
