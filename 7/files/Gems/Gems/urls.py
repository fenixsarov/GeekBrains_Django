"""Gems URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
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
from mainApp.views import gems, main, listing
from userManagementApp.views import *
from adminApp.views import *

urlpatterns = [
    url(r'^$', main),
]

urlpatterns += [
    url(r'^user/login/$', login),
    url(r'^user/logout/$', logout),
    # url(r'^user/registration/$', registration_low),
    url(r'^user/registration/$', registration),
    url(r'^admin/$', admin_page, name='admin_users'),
    url(r'^admin/delete/user/(\d+)$', delete_user),
    url(r'^admin/get_user_form/(\d+)$', get_user_form),
    url(r'^admin/create/user/(\d*)$', create_user),
]

urlpatterns += [
    url(r'admin/gems/', admin_gems, name='admin_gems'),
    url(r'^admin/create/gems$', admin_gems_create, name='gems_create'),
    url(r'^admin/delete/gems/(\d+)$', admin_gems_delete, name='gems_delete'),
    url(r'^admin/update/gems/(\d+)$', admin_gems_update, name='gems_update'),
    url(r'^admin/detail/gems/(\d+)$', admin_gems_detail, name='gems_detail')
]

urlpatterns += [
    url(r'^gems/(\d+)/$', gems, name='gems')
]

urlpatterns += [
    url(r'^contacts/$', listing)
]

# Данный подход нерекомендуется, и будет убран в django 1.10
# urlpatterns = patterns('mainApp.views',
#     url(r'^$', 'main'),
# )
