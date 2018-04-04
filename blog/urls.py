from django.contrib import admin
from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.index),
    path('detail',views.detail,name = 'detail'),
    path('blog',views.blog.as_view(),name = 'blog'),
]