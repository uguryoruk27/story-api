from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import ugettext_lazy as _


class Profile(AbstractUser):

    picture = models.ImageField(_("Profile Picture"),
                                upload_to="users/avatars/",
                                null=True, blank=True)

    def __unicode__(self):
        return u"%s" % self.username