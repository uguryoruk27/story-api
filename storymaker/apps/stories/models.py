from django.db import models
from django.conf import settings
from django.utils.translation import ugettext_lazy as _

from rest_framework.reverse import reverse

class Story(models.Model):
	"""
		Contains story details
	"""
	title = models.CharField(_("Title"), max_length=120)
	owner = models.ForeignKey(settings.AUTH_USER_MODEL, verbose_name=_("Creater"), related_name="stories", null=True, blank=True)

	def __unicode__(self):
		return "%s" % (self.title)


class PageNode(models.Model):
	"""
		A story consists of pagenodes.
	"""
	title = models.CharField(_("Title"), max_length=120)
	story = models.ForeignKey(Story, verbose_name=_("Story"), related_name="pages")

	def __unicode__(self):
		return "%s" % self.title

ELEMENT_CHOICES = (
	('text', 'Text'),
	('quote', 'Quote'),
	('image', 'Image')
)

class ElementNode(models.Model):
	"""
		A node consists of elements. Element types : text, quote, image
	"""
	pagenode = models.ForeignKey(PageNode, verbose_name=_("Page"), related_name="elements")
	ordering = models.IntegerField(_("Order"), null=True, blank=True)
	type = models.CharField(_("Type"), max_length=30, choices=ELEMENT_CHOICES)
	image = models.ImageField(_("Element Image"), upload_to="elements/images/", null=True, blank=True)
	content = models.CharField(_("Content"), max_length=500, null=True, blank=True)

	def __unicode__(self):
		return u"%s - element" % self.pagenode.title

	def get_content(self):
		if self.type == "image":
			return ""
		else:
			return self.content


class LinkNode(models.Model):
	"""
		Links are the choices presented to the user.
	"""
	pagenode = models.ForeignKey(PageNode, verbose_name=_("Page"), related_name="links")
	ordering = models.IntegerField(_("Ordering"), null=True, blank=True)
	linked_pagenode = models.ForeignKey(PageNode, verbose_name=_("Linked Page"), related_name="target_links")
	content = models.CharField(_("Content"), max_length=200)

	def __unicode__(self):
		return "%s" % (self.content)
