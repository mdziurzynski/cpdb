from django.conf.urls import url, include

from cpdb_core.views import HomeView, ContactView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
]
