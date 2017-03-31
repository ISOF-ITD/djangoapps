from django.conf.urls import url
from ..views import (FrFragasvarListView, FrFragasvarCreateView, FrFragasvarDetailView,
                     FrFragasvarUpdateView, FrFragasvarDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(FrFragasvarCreateView.as_view()),
        name="fr_fragasvar_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(FrFragasvarUpdateView.as_view()),
        name="fr_fragasvar_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(FrFragasvarDeleteView.as_view()),
        name="fr_fragasvar_delete"),

    url(r'^(?P<pk>\d+)/$',
        FrFragasvarDetailView.as_view(),
        name="fr_fragasvar_detail"),

    url(r'^$',
        FrFragasvarListView.as_view(),
        name="fr_fragasvar_list"),
]
