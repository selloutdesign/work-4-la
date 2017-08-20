from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from .views import CreateView, DetailsView, DetailView, jobsearch, JobFilter, AuthListView

urlpatterns = {
    url(r'^jobs/$', CreateView.as_view(), name="create"),
    url(r'^auth/jobs/$', AuthListView.as_view(), name="auth-job-list"),
    url(r'^jobs/api/(?P<pk>[0-9]+)/$',
        DetailsView.as_view(), name = "detail-api"),
    url(r'^jobs/(?P<pk>[0-9]+)/$',
        DetailView.as_view(), name = "detail"),
    url(r'^job-list/$', jobsearch, name='job-list'),
}

urlpatterns = format_suffix_patterns(urlpatterns)