from django.conf.urls import url, include

from cpdb_args.views import ARGHomeView, AntibioticClassView, ARGeneView, InputFileView, InputFileConfirmView

urlpatterns = [
    url(r'^$', ARGHomeView.as_view(), name='args_home'),
    url(r'^ab_class/(?P<antibiotic_class_id>[0-9]+)/$', AntibioticClassView.as_view(), name='args_antibiotic_class'),
    url(r'^argene/(?P<argene_id>[0-9]+)/$', ARGeneView.as_view(), name='args_argene'),
    url(r'^args_file_upload/$', InputFileView.as_view(), name="args_file_upload"),
    url(r'^args_file_upload/(?P<inputfile_id>[0-9]+)/$', InputFileConfirmView.as_view(), name='args_file_upload_check'),
    # url(r'^args/', include('cpdb.cpdb_args.urls')),
    # url(r'^notification_email_success/$', HomeView.as_view(template_name="cpdb_core/notification_email_success.html")),
    # url(r'^argp_classes/$', ARClassListView.as_view(), name='argp_classes_list'),
    # url(r'^argp_classes/(?P<pk>[-\w]+)/$', ARClassDetailView.as_view(), name='argp_classes_detail'),
    # url(r'^argp_classes/targetgene/(?P<pk>[-\w]+)/$', TargetGeneDetailView.as_view(), name='targetgene_detail'),
    # url(r'^download$', FileLinkListView.as_view(), name='download'),
    # url(r'^contact$', ContactView.as_view(), name='contact'),
]
