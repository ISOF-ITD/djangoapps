from django.conf.urls import url
from ..views import (AreArendeListView, AreArendeCreateView, AreArendeDetailView,
                     AreArendeUpdateView, AreArendeDeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(AreArendeCreateView.as_view()),
        name="are_arende_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(AreArendeUpdateView.as_view()),
        name="are_arende_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(AreArendeDeleteView.as_view()),
        name="are_arende_delete"),

    url(r'^(?P<pk>\d+)/$',
        AreArendeDetailView.as_view(),
        name="are_arende_detail"),

    url(r'^$',
        AreArendeListView.as_view(),
        name="are_arende_list"),
]
