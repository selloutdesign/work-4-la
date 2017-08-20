from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from django.views.generic import TemplateView
from .views import SignUp, GroupViewSet

urlpatterns = {
    url(r'^sign_up/$', SignUp.as_view(), name="sign_up"),
    url(r'^groups', GroupViewSet.as_view(), name="groups")
}

urlpatterns = format_suffix_patterns(urlpatterns)