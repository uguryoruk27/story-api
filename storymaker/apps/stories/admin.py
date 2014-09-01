from django.contrib import admin

from apps.stories.models import *

admin.site.register(Story)
admin.site.register(PageNode)
admin.site.register(ElementNode)
admin.site.register(LinkNode)