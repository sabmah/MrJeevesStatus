from django.conf.urls import patterns, url
from MrJeevesApp import views

urlpatterns = patterns('',
        url(r'^$', views.index, name='index'),
        url(r'^ROSActionOutput/', views.index, name='ROSActionOutput'))