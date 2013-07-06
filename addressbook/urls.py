from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import contacts.views


urlpatterns = patterns('',
    url(r'^$', contacts.views.ListContactView.as_view(),
        name='contacts-list',),
    url(r'^new$', contacts.views.CreateContactView.as_view(),
        name='contacts-new',),
)

urlpatterns += staticfiles_urlpatterns()
