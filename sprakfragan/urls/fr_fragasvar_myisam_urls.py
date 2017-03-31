from django.conf.urls import url
from ..views import (FrFragasvarMyisamListView, FrFragasvarMyisamCreateView, FrFragasvarMyisamDetailView,
                     FrFragasvarMyisamUpdateView, FrFragasvarMyisamDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(FrFragasvarMyisamCreateView.as_view()),
        name="fr_fragasvar_myisam_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(FrFragasvarMyisamUpdateView.as_view()),
        name="fr_fragasvar_myisam_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(FrFragasvarMyisamDeleteView.as_view()),
        name="fr_fragasvar_myisam_delete"),

    url(r'^(?P<pk>\d+)/$',
        FrFragasvarMyisamDetailView.as_view(),
        name="fr_fragasvar_myisam_detail"),

    url(r'^$',
        FrFragasvarMyisamListView.as_view(),
        name="fr_fragasvar_myisam_list"),
]
