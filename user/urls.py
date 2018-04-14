from django.urls import path, re_path

from . import views

app_name = 'users'

urlpatterns = [
    path('register/',views.register_user,name='register'),
    path('index/',views.index,name='index'),
    path('pubication',views.pubilcation,name='publication'),
    path('pubication_done',views.pubication_done,name='publication_done'),
    path('post_manage',views.post_manage,name='post_manage'),
    re_path('^post_delete/(?P<post_pk>\d+)/$',views.post_delete,name='post_delete')
]