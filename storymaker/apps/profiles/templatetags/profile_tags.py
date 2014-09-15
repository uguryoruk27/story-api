from django import template
from django.conf import settings
from django.contrib.contenttypes.models import ContentType

register = template.Library()

@register.assignment_tag
def user_stories(user):

	if user.is_authenticated():
		return user.stories.all()

	return []
