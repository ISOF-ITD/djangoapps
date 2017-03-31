from django.conf.urls import include, url

urlpatterns = [

    url(r'^fr_fragasvar_test1_s/', include('sprakfragan.urls.fr_fragasvar_test1_urls')),  # NOQA
    url(r'^fr_fragasvars/', include('sprakfragan.urls.fr_fragasvar_urls')),
    url(r'^fr_fragasvar_myisams/', include('sprakfragan.urls.fr_fragasvar_myisam_urls')),
    url(r'^date_test2_s/', include('sprakfragan.urls.date_test2_urls')),
    url(r'^are_arendes/', include('sprakfragan.urls.are_arende_urls')),
    url(r'^are_inlaggs/', include('sprakfragan.urls.are_inlagg_urls')),
    url(r'^nyckelords/', include('sprakfragan.urls.nyckelord_urls')),
    url(r'^date_tests/', include('sprakfragan.urls.date_test_urls')),
]
