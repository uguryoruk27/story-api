from rest_framework import serializers

from apps.stories.models import Story, PageNode, LinkNode, ElementNode

class StorySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Story
        fields = ("id", "title", "pages")

class PageNodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PageNode
        fields = ("id", "title", "story", "elements", "links")

class LinkNodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = LinkNode
        fields = ("id", "pagenode", "ordering", "linked_pagenode", "content")

class ElementNodeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ElementNode
        fields = ("id", "pagenode", "ordering", "image", "content", "type")




