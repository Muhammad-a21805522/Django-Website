from django.shortcuts import render
from . import views
from django.urls import path

app_name = "website"

urlpatterns = [
    path('', views.home_page_view, name='home'),
    path('intro', views.intro_page_view, name='intro'),
    path('multi', views.multi_page_view, name='multi')
]