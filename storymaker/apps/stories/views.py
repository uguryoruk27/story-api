from django.shortcuts import render, redirect, render_to_response
from django.http import Http404
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic.edit import UpdateView, CreateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.utils.decorators import method_decorator
from django.template import RequestContext

from apps.stories.forms import CreateStoryForm, CreatePageForm
from apps.stories.models import Story, PageNode



class CreateStory(CreateView):
    template_name = "stories/create.html"
    model = Story
    form_class = CreateStoryForm

    def get_success_url(self):
        return "/"

    def form_valid(self, form):
        self.object = form.instance
        # started by
        self.object.owner = self.request.user
        self.object.save()
        return super(CreateStory, self).form_valid(form)

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(CreateStory, self).dispatch(*args, **kwargs)

class StoryDetails(DetailView):
    template_name = "stories/details.html"
    model = Story
    slug_field = "slug"

class StoryList(ListView):
    template_name = "stories/story_list.html"
    model = Story
    queryset = Story.objects.all()


class CreatePage(CreateView):
    template_name = "pages/create.html"
    model = PageNode
    form_class = CreatePageForm

    def get_success_url(self):
        return "/"

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(CreatePage, self).dispatch(*args, **kwargs)

class PageDetails(DetailView):
    template_name = "pages/details.html"
    model = PageNode
    slug_field = "slug"


ITEMS = ()

def edit_page(request, pk, template="pages/edit.html"):

    try:
        page = PageNode.objects.get(pk=pk)
    except:
        page = None

    if not page:
        raise Http404("No such page.")

    if request.method == "POST":


        raise Exception(request.POST)




    ctx = {
        "page" : page,
    }

    return render_to_response(template, ctx, context_instance=RequestContext(request))




