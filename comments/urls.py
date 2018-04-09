
from django.urls import path,re_path
from . import views

app_name = 'comments'

urlpatterns = [
    re_path(r'comment/post/(?P<post_pk>\d+)/$', views.post_comment, name='post_comment'),
]