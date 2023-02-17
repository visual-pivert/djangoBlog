from django.shortcuts import render, redirect, HttpResponse
from django.contrib.auth.views import LoginView, login_required
from django.urls import reverse_lazy, reverse
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect,JsonResponse
from .forms import InfluenceurForm
from .models import Influenceur
import datetime

from django.contrib import admin
from django.contrib.auth import authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
# from django.template.context_processors import request
#from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from django.views import generic


class Login(LoginView):
    template_name = "blog/login.html"
    model = Influenceur()
    fields = "__all__"
    redirect_to = "workspace"

    def get_success_url(self):
        if self.request.user:
            if self.request.user.is_staff:
                return reverse_lazy("admin")
            return reverse_lazy("blog:workspace")
        else:
            print('Tsy user')
        return reverse_lazy("workspace")



def log_in (request):
    if request.method =='POST':
        username = request.POST['username']
        pwd = request.POST['password']
        # print(username, pwd)
        user = authenticate(username=username, password=pwd)
        if user:
            login(request, user)
            return HttpResponseRedirect(reverse('workspace'))
    return render(request, 'blog/login.html')


# @login_required
def workspace (request):
    user = request.user
    return render(request, 'blog/workspace.html', {'user': f'bjr{user}'})


"""def signup (request):
        if request.method == 'GET':
            form = InfluenceurRegisterForm()
            return render(request, 'blog/signup.html')

        if request.method =='POST':
            form = InfluenceurRegisterForm(request.POST)
            if form.is_valid():
                # user = form.save(commit=False)
                # user.username = user.username.lower()
                name = request.POST['username']
                past = request.POST['birth']
                sex = request.POST['sex']
                mail = request.POST['mail']
                pass1 = request.POST['password']
                pass2 = request.POST['cpassword']
                user = Influenceur(username=name, date_of_birth=past, sex=sex, email=mail, date_joined=datetime.now,
                password=pass1)
                user.save()
                # messages.success(request, 'singup successfully ^_^')
                login(request, user)
                return redirect('workspace/')
            else:
                return render(request,'blog/signup.html')"""

"""
class SignUp(CreateView):
    model = Influenceur
    template_name = "templates/signup.html"
    form_class = InfluenceurRegisterForm
    success_url = reverse_lazy('blog:workspace')
"""
class SignUp(generic.CreateView):
    form_class = Influenceur
    succes_url= reverse_lazy("workspace")
    template_name = "blog/signup.html"

def signup(request):
    form = InfluenceurForm()
    if request.method == 'POST':
        form = InfluenceurForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get("username")
            pssw = form.cleaned_data.get("password")
            # mail = form.cleaned_data.get("email")
            # sexe = form.cleaned_data.get("sex_choices")
            # date_of_birth = form.clean_data.get("date_of_birth")
            user = authenticate(username=username, password=pssw)
            login(request, user)
            return redirect('workspace')
        else:
            form = InfluenceurForm()
    return render(request, 'blog/signup.html', {'form':form})

"""


def signup(request):
    registerForm = InfluenceurRegisterForm()
    if request.method == 'POST':
        registerForm = InfluenceurRegisterForm(request.POST)
        if registerForm.is_valid():
                name = request.POST['username']
                past = request.POST['birth']
                sex = request.POST['sex']
                mail = request.POST['mail']
                pass1 = request.POST['password']
                pass2 = request.POST['cpassword']
                user = Influenceur.objects.create()(username=name, date_of_birth=past, sex=sex, email=mail, date_joined=datetime.now,
                password=pass1)
                user.save()
        else:
            registerForm = InfluenceurRegisterForm()
    return render(request, 'blog/signup.html', {'form': registerForm})
"""


def logout_view(request):
    logout(request) 
    return HttpResponse('you are out, now!')

@login_required()
def accueil (request):
    return HttpResponse('you are in!')
