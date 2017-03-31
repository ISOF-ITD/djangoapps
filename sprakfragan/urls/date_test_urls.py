from django.conf.urls import url
from ..views import (DateTestListView, DateTestCreateView, DateTestDetailView,
                     DateTestUpdateView, DateTestDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(DateTestCreateView.as_view()),
        name="date_test_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(DateTestUpdateView.as_view()),
        name="date_test_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(DateTestDeleteView.as_view()),
        name="date_test_delete"),

    url(r'^(?P<pk>\d+)/$',
        DateTestDetailView.as_view(),
        name="date_test_detail"),

    url(r'^$',
        DateTestListView.as_view(),
        name="date_test_list"),
]
