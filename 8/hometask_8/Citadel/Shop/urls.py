from django.conf.urls import url
from .views import main, listing, units, catalog, login_page

urlpatterns = [
    url(r'^$', main, name='index'),
    url(r'^contacts/$', listing, name='contacts'),
    url(r'^units/(\d+)/$', units, name='units'),
    url(r'^catalog/$', catalog, name='catalog'),
    url(r'^user/login_page/$', login_page, name='login_page'),
]
