from django.conf.urls import url, include
from .views import *
from .views import UnitsListView, UnitsDeleteView, UnitsCreateView, UnitsDetailView, UnitsUpdateView

urlpatterns = [
    url(r'^$', admin_page),
    url(r'^delete/user/(\d+)$', delete_user),
    url(r'^get_user_form/(\d+)/$', get_user_form),
    url(r'^create/user/(\d+)$', create_user),
    # url(r'units/', admin_units, name='admin_units'),
    url(r'units/$', UnitsListView.as_view(), name='admin_units'),
    url(r'^create/$', UnitsCreateView.as_view(), name='units_create'),
    url(r'^delete/(?P<pk>\d+)$', UnitsDeleteView.as_view(), name='units_delete'),
    url(r'^update/(?P<pk>\d+)$', UnitsUpdateView.as_view(), name='units_update'),
    url(r'^detail/(?P<pk>\d+)$', UnitsDetailView.as_view(), name='units_detail')
]
