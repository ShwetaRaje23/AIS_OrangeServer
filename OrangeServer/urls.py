from django.conf.urls import patterns, include, url
from django.contrib import admin
import storyAgent
from classes import messages

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'OrangeServer.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^tellMeAStory/$', storyAgent.tellMeAStory),
    url(r'^talk/$', messages.talk),
    url(r'^admin/', include(admin.site.urls)),
)
