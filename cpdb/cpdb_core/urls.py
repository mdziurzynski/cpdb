from django.conf.urls import url

from cpdb_core.views import HomeView, ContactView, ARClassListView, ARClassDetailView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^argp_classes/$', ARClassListView.as_view(), name='argp_classes_list'),
    url(r'^argp_classes/(?P<pk>[-\w]+)/$', ARClassDetailView.as_view(), name='argp_classes_detail'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
]