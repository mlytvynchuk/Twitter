from django.shortcuts import render
from django.db import models
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from .models import Twitt,User
from django.views.generic import ListView,DetailView,CreateView,UpdateView


# Create your views here.

# def home(request):
#     context = {
#         'posts': Twitt.objects.all(),
#
#     }
#     return render(request,'blog/home.html',context)
#

class TwittListView(ListView):
    model = Twitt
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']

class TwittDetailView(DetailView):
    model = Twitt
    template_name = 'blog/twitt-detail.html'

class TwittCreateView(LoginRequiredMixin,CreateView):
    model = Twitt
    titleView = 'Create twitt'
    buttonView = 'Create'
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['titleView'] = self.titleView
        ctx['buttonView'] = self.buttonView
        return ctx


class TwittUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Twitt
    titleView = 'Update twitt'
    buttonView = 'Update'
    fields = ['title','content']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx['titleView'] = self.titleView
        ctx['buttonView'] = self.buttonView
        return ctx

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False





def about(request):
    return render(request,'blog/about.html',{'title':'About'})