from django.conf.urls import url
from ..views import (NyckelordListView, NyckelordCreateView, NyckelordDetailView,
                     NyckelordUpdateView, NyckelordDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(NyckelordCreateView.as_view()),
        name="nyckelord_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(NyckelordUpdateView.as_view()),
        name="nyckelord_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(NyckelordDeleteView.as_view()),
        name="nyckelord_delete"),

    url(r'^(?P<pk>\d+)/$',
        NyckelordDetailView.as_view(),
        name="nyckelord_detail"),

    url(r'^$',
        NyckelordListView.as_view(),
        name="nyckelord_list"),
]
