from django.conf.urls import url, include
from .views import admin_page, delete_user, get_user_form, create_user, GemsCreateView, \
    GemsDeleteView, GemsDetailView, GemsUpdateView, GemsListView

urlpatterns = [
    url(r'gems/$', GemsListView.as_view(), name='admin_gems'),
    url(r'^gems/create/$', GemsCreateView.as_view(), name='gems_create'),
    url(r'^gems/delete/(?P<pk>\d+)/$', GemsDeleteView.as_view(), name='gems_delete'),
    url(r'^gems/update/(?P<pk>\d+)/$', GemsUpdateView.as_view(), name='gems_update'),
    url(r'^gems/detail/(?P<pk>\d+)/$', GemsDetailView.as_view(), name='gems_detail'),
    url(r'^$', admin_page, name='admin_users'),
    url(r'^delete/user/(\d+)/$', delete_user),
    url(r'^get_user_form/(\d+)/$', get_user_form),
    url(r'^create/user/(\d*)/$', create_user)
]
