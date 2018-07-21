from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.shortcuts import render, redirect
from .forms import Round1Form, Round2Form, Round3Form, UserForm
from .models import Round1, Round2, Round3
from django.views.generic.edit import CreateView, UpdateView
from django import forms
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from django.template import RequestContext

def logout_user(request):
    logout(request)
    return render(request, 'music/login.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                round1 = Round1.objects.filter(user=request.user)
                return render(request, 'music/index.html', {'round1': round1})
            else:
                return render(request, 'music/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'music/login.html', {'error_message': 'Invalid login'})
    return render(request, 'music/login.html')


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'music/login.html')
    else:
        return render(request, 'music/index.html')

class Round1View(CreateView):
    model = Round1
    fields = ['con1', 'con2', 'con3', 'con4', 'con5', 'con6', 'con7','con8','con9','con10']

    def form_valid(self, form):
        user = self.request.user
        obj = form.save(commit=False)
        obj.user = user
        obj.save()
        return render(self.request, 'music/index.html')


class Round2View(CreateView):
    model = Round2
    fields = ['con1', 'con2', 'con3', 'con4', 'con5', 'con6', 'con7','con8','con9','con10']

    def form_valid(self, form):
        user = self.request.user
        obj = form.save(commit=False)
        obj.user = user
        obj.save()
        return render(self.request, 'music/index.html')


class Round3View(CreateView):
    model = Round3
    fields = ['con1', 'con2', 'con3', 'con4', 'con5', 'con6', 'con7', 'con8','con9','con10']

    def form_valid(self, form):
        user = self.request.user
        obj = form.save(commit=False)
        obj.user = user
        obj.save()
        return render(self.request, 'music/index.html')
