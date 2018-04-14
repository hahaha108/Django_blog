from django.urls import path

from . import views

app_name = 'users'

urlpatterns = [
    path('register/',views.register_user,name='register'),
    path('index/',views.index,name='index'),
    path('pubication',views.pubilcation,name='publication'),
    path('pubication_done',views.pubication_done,name='publication_done')
]