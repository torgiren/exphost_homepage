from django.conf.urls import patterns, include, url
from django.contrib import admin
#import exphost.core.views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'exphost.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'exphost.core.views.home', name='home'),

    url(r'^admin/', include(admin.site.urls)),
)
