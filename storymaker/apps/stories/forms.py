import re

from django import forms
from django.utils.translation import ugettext_lazy as _

from apps.stories.models import Story, PageNode
"""
class CreateAdvertForm(forms.ModelForm):
    
    story_image = forms.ImageField(label=_(u"Image"))

    class Meta:
        model = Advert
        exclude = ("owner", "is_active", "slug", "date_created", "tags")

    def __init__(self, *args, **kwargs):
        super(CreateAdvertForm, self).__init__(*args, **kwargs)

        self.fields["title"].required = True
        self.fields["description"].required = True


    def save(self, commit=True):

        # handle tags
        try:
            tags = self.cleaned_data["advert_tags"].split(",")

            for tag in tags:
                if tag.strip():
                    t, e = Tag.objects.get_or_create(name=tag)
                    t.save()
                    self.instance.tags.add(t)
        except Exception as e:
            pass

        # handle images
        try:
            img = self.cleaned_data["advert_image"]

            advert_image = AdvertImage()
            advert_image.picture = img
            advert_image.advert = self.instance
            advert_image.save()

            self.instance.images.add(advert_image)
        except:
            pass

        super(CreateAdvertForm, self).save(commit)

"""


class CreateStoryForm(forms.ModelForm):

    class Meta:
        model = Story
        fields = ("title",)


class CreatePageForm(forms.ModelForm):

    class Meta:
        model = PageNode
        fields = ("title",)
