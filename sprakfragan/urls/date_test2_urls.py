from django.conf.urls import url
from ..views import (DateTest2ListView, DateTest2CreateView, DateTest2DetailView,
                     DateTest2UpdateView, DateTest2DeleteView)
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^create/$',  # NOQA
        login_required(DateTest2CreateView.as_view()),
        name="date_test2_create"),

    url(r'^(?P<pk>\d+)/update/$',
        login_required(DateTest2UpdateView.as_view()),
        name="date_test2_update"),

    url(r'^(?P<pk>\d+)/delete/$',
        login_required(DateTest2DeleteView.as_view()),
        name="date_test2_delete"),

    url(r'^(?P<pk>\d+)/$',
        DateTest2DetailView.as_view(),
        name="date_test2_detail"),

    url(r'^$',
        DateTest2ListView.as_view(),
        name="date_test2_list"),
]
