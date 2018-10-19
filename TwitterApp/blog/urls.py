"""TwitterApp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from django.urls import path
from .views import TwittListView,TwittDetailView,TwittCreateView,TwittUpdateView,TwittDeleteView
from . import views


urlpatterns = [
    path('', TwittListView.as_view(),name='blog-home'),
    path('twitt/<int:pk>', TwittDetailView.as_view(), name='twitt-detail'),
    path('twitt/new/', TwittCreateView.as_view(), name='twitt-create'),
    path('twitt/<int:pk>/update/', TwittUpdateView.as_view(), name='twitt-update'),
    path('twitt/<int:pk>/delete/', TwittDeleteView.as_view(), name='twitt-delete'),
    path('about/', views.about, name='blog-about'),

]
