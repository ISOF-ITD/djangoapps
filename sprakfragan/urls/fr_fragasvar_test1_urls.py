from django.conf.urls import url
from ..views import (FrFragasvarTest1ListView, FrFragasvarTest1CreateView, FrFragasvarTest1DetailView,
                     FrFragasvarTest1UpdateView, FrFragasvarTest1DeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(FrFragasvarTest1CreateView.as_view()),
        name="fr_fragasvar_test1_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(FrFragasvarTest1UpdateView.as_view()),
        name="fr_fragasvar_test1_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(FrFragasvarTest1DeleteView.as_view()),
        name="fr_fragasvar_test1_delete"),

    url(r'^(?P<pk>\d+)/$',
        FrFragasvarTest1DetailView.as_view(),
        name="fr_fragasvar_test1_detail"),

    url(r'^$',
        FrFragasvarTest1ListView.as_view(),
        name="fr_fragasvar_test1_list"),
]
