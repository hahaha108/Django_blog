from django.contrib import admin
from django.urls import path,re_path
from . import views

app_name = 'myblog'

urlpatterns = [
    path('', views.index,name = 'index'),
    re_path('^detail/(?P<pk>\d+)/$',views.detail.as_view(),name = 'detail'),
    path('blog',views.blog.as_view(),name = 'bloglist'),
]