from django.conf.urls import *

from apps.stories.views import CreateStory, StoryDetails,\
			CreatePage, PageDetails, edit_page, run_story

urlpatterns = patterns('',

    url(r'^create/$', CreateStory.as_view(), name="create_story"),
    url(r'^details/(?P<pk>[\d-]+)/$', StoryDetails.as_view(), name="story_details"),

    url(r'^page/create/(?P<pk>[\d-]+)/$', CreatePage.as_view(), name="create_page"),
    url(r'^page/details/(?P<pk>[\d-]+)/$', PageDetails.as_view(), name="page_details"),
    url(r'^page/edit/(?P<pk>[\d-]+)/$', edit_page, name="edit_page"),

    url(r'^run/(?P<story_id>[\d-]+)/(?P<page_id>[\d-]+)', run_story, name="run_story"),

)