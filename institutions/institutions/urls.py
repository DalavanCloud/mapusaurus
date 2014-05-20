from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'institutions.views.home', name='home'),
    url(r'^institutions/', include('respondants.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^shapes/', include('geo.urls'))
)
