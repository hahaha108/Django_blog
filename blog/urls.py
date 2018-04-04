from django.contrib import admin
from django.urls import path
from . import views

app_name = 'myblog'

urlpatterns = [
    path('', views.index,name = 'index'),
    path('detail',views.detail,name = 'detail'),
    path('blog',views.blog.as_view(),name = 'bloglist'),
]