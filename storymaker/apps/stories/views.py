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
from apps.stories.models import Story, PageNode, ElementNode



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



class CreatePage(CreateView):
    template_name = "pages/create.html"
    model = PageNode
    form_class = CreatePageForm

    def get_success_url(self):
        return reverse("story_details", kwargs={"pk": self.kwargs["pk"]})

    def form_valid(self, form):
        self.object = form.instance
        # started by
        self.object.story_id = int(self.kwargs["pk"])
        self.object.save()
        return super(CreatePage, self).form_valid(form)

    @method_decorator(login_required())
    def dispatch(self, *args, **kwargs):
        return super(CreatePage, self).dispatch(*args, **kwargs)


ITEMS = ()

def edit_page(request, pk, template="pages/edit.html"):

    try:
        page = PageNode.objects.get(pk=pk)
    except:
        raise Http404("No such page.")

    if request.method == "POST":

        # handle text
        for k, v in request.POST.dict().items():

            if k.startswith("formitem"):
                
                vals = k.split("-")
                item_type, item_id, item_is_new, item_order = vals[1], vals[2], (vals[2] == "0"), vals[3]

                if item_is_new:
                    e = ElementNode()
                    e.content = v
                    e.pagenode_id = page.id
                    e.type = item_type
                    e.ordering = int(item_order)
                    e.save()
                else:
                    element = get_element(item_id, page.id)

                    if element:
                        element.content = v
                        element.ordering = int(item_order)
                        element.save()
                    else:
                        print "no such element"

        # handle images
        for k, v in request.FILES.dict().items():
            print k, " --- ", v
            if k.startswith("formitem"):
                vals = k.split("-")
                item_type, item_id, item_is_new, item_order = vals[1], vals[2], (vals[2] == "0"), vals[3]

                if item_is_new:
                    e = ElementNode()
                    e.pagenode_id = page.id
                    e.type = item_type
                    e.ordering = int(item_order)
                    e.save()
                    e.image.save(v.name, v)
                else:
                    e = get_element(item_id, page.id)
                    e.image.save(v.name, v)
                    e.ordering = item_order
                    e.save()


    ctx = {
        "page" : page,
    }

    return render_to_response(template, ctx, context_instance=RequestContext(request))




def get_element(id, pagenode_id):

    try:
        return ElementNode.objects.get(id=id, pagenode_id=pagenode_id)
    except:
        return None
