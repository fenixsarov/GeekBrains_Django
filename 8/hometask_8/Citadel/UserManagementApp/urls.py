from django.conf.urls import url
from .views import login, logout, registration_low, registration

urlpatterns = [
    url(r'^login/$', login),
    url(r'^logout/$', logout),
    url(r'^registration/$', registration_low),
    url(r'^registration-form/$', registration)
]
