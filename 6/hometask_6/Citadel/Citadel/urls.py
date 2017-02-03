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
from django.contrib import admin
from Shop.views import *
from administrationApp.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', main, name='index'),
    url(r'^user/login_page/$', login_page, name='login_page'),
    url(r'^user/login/$', login),
    url(r'^user/logout/$', logout, name='logout'),
    url(r'^user/registration/$', registration_low),
    url(r'^user/registration-form/$', registration),
    url(r'^adminka/$', admin_page),
    url(r'^adminka/delete/user/(\d+)$', delete_user)
]
