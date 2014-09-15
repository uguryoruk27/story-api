from django.conf.urls import *

from apps.profiles.views import UpdateProfile

urlpatterns = patterns('',

    # users
    url(r'^register/$', 'apps.profiles.views.register_user', name="register"),
    url(r'^login/$', 'apps.profiles.views.login_user', name="login"),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}, name="logout"),
    url(r'^password_change/$', 'django.contrib.auth.views.password_change', name='password_change'),
    url(r'^password_change/done/$', 'django.contrib.auth.views.password_change_done', name='password_change_done'),
    url(r'^update/$', UpdateProfile.as_view(), name="update_profile"),

    url(r'^view/(?P<user_id>[-\d]+)/$', 'apps.profiles.views.view_profile', name="view_profile"),

)