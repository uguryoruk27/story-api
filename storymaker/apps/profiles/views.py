
from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.views.generic.edit import UpdateView

from apps.profiles.decorators import anonymous_required
from apps.profiles.forms import *

#from birineyarar.settings import EMAIL_HOST_USER

@anonymous_required('index')
def login_user(request, login_success_url="/", template="login.html"):
    """ 
    	Login view 
    """
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(username=username, password=password)
        form = LoginForm(request.POST)
        if user is not None:
            login(request, user)
            return redirect(login_success_url)
    else:
        form = LoginForm()
    
    return render(request, template, {'form': form})


@anonymous_required('index')
def register_user(request, register_success_url="/", template="register.html"):
    """
    	Registration view
    """
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password1']

            user = Profile.objects.create_user(
                username=username,
                email=email,
                password=password)

            user.save()

            subject = "Welcome"

            recipients = [email,]


            auth_usr = authenticate(username=username,
                                    password=password)

            if auth_usr:
                login(request, auth_usr)
            
            return redirect(register_success_url)
    else:
        form = RegistrationForm()
    
    return render(request, template, {'form': form})



@login_required
def profile_details(request, template="profiles/profile_details.html"):
    form = NewProjectForm()
    ctx = {'profile': request.user,
           'form': form}

    return render(request, template, ctx)


def view_profile(request, user_id, template="profiles/view.html"):

    try:
        profile = Profile.objects.get(pk=user_id)
    except:
        profile = None
        return redirect(reverse("index"))

    ctx = {
        'profile' : profile,
        '' : '',
    }

    return render(request, template, ctx)


def home(request, template="home.html"):

    ctx = {}

    return render(request, template, ctx)



class UpdateProfile(UpdateView):

    model = Profile
    form_class = UpdateProfileForm
    template_name = "profiles/update.html"

    def get_success_url(self):
        return reverse('update_profile')

    def get_object(self, queryset=None):
        if self.request:
            return self.request.user
        return None
