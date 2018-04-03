from django.urls import path

from . import views

urlpatterns = [
    path(r'register/',views.register_user),
    path(r'info/',views.info_user),
    path(r'login/',views.login),
    path(r'logout/',views.logout),
]