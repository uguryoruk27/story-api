from django.shortcuts import render

from rest_framework import viewsets, filters, status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from apps.stories.models import Story, PageNode, ElementNode, LinkNode
from apps.stories.serializers import StorySerializer, PageNodeSerializer, ElementNodeSerializer, LinkNodeSerializer


class StoryViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Story.objects.all()
    serializer_class = StorySerializer
    filter_fields = ("id",)

class PageNodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = PageNode.objects.all()
    serializer_class = PageNodeSerializer
    filter_fields = ("id",)

class ElementNodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = ElementNode.objects.all()
    serializer_class = ElementNodeSerializer

class LinkNodeViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = LinkNode.objects.all()
    serializer_class = LinkNodeSerializer

