from django.conf.urls import url

from cpdb_core.views import HomeView, ContactView, ARClassListView, ARClassDetailView, \
    TargetGeneDetailView, FileLinkListView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^notification_email_success/$', HomeView.as_view(template_name="cpdb_core/notification_email_success.html")),
    url(r'^argp_classes/$', ARClassListView.as_view(), name='argp_classes_list'),
    url(r'^argp_classes/(?P<pk>[-\w]+)/$', ARClassDetailView.as_view(), name='argp_classes_detail'),
    url(r'^argp_classes/targetgene/(?P<pk>[-\w]+)/$', TargetGeneDetailView.as_view(), name='targetgene_detail'),
    url(r'^download$', FileLinkListView.as_view(), name='download'),
    url(r'^contact$', ContactView.as_view(), name='contact'),
]
