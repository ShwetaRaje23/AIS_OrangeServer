from django.conf.urls import patterns, include, url
from django.contrib import admin
import storyAgent


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OrangeServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^tellMeAStory/', include('storyAgent.tellMeAStory')),
    url(r'^admin/', include(admin.site.urls)),
)
