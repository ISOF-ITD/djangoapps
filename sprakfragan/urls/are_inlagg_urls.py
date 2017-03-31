from django.conf.urls import url
from ..views import (AreInlaggListView, AreInlaggCreateView, AreInlaggDetailView,
                     AreInlaggUpdateView, AreInlaggDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(AreInlaggCreateView.as_view()),
        name="are_inlagg_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(AreInlaggUpdateView.as_view()),
        name="are_inlagg_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(AreInlaggDeleteView.as_view()),
        name="are_inlagg_delete"),

    url(r'^(?P<pk>\d+)/$',
        AreInlaggDetailView.as_view(),
        name="are_inlagg_detail"),

    url(r'^$',
        AreInlaggListView.as_view(),
        name="are_inlagg_list"),
]
