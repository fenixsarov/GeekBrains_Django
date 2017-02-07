"""Citadel URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/dev/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from Shop.views import *
from administrationApp.views import *

urlpatterns = [
    url(r'^$', main, name='index'),
    url(r'^contacts/$', listing, name='contacts'),
]

urlpatterns += [
    url(r'^user/login_page/$', login_page, name='login_page'),
    url(r'^user/login/$', login),
    url(r'^user/logout/$', logout),
    # url(r'^user/registration/$', registration_low),
    url(r'^user/registration-form/$', registration),
    url(r'^admin/$', admin_page),
    url(r'^admin/delete/user/(\d+)$', delete_user),
    url(r'^admin/get_user_form/(\d+)$', get_user_form),
    url(r'^admin/create/user/(\d+)$', create_user),

]

urlpatterns += [
    url(r'^catalog/$', catalog, name='catalog'),
    url(r'^units/(\d+)/$', units, name='units'),
    url(r'admin/units/', admin_units, name='admin_units'),
    url(r'^admin/create/units$', admin_units_create, name='units_create'),
    url(r'^admin/delete/units/(\d+)$', admin_units_delete, name='units_delete'),
    url(r'^admin/update/units/(\d+)$', admin_units_update, name='units_update'),
    url(r'^admin/detail/units/(\d+)$', admin_units_detail, name='units_detail')
]