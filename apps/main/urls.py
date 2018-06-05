from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.loginView, name='login'),
    url(r'^logout/$', views.logoutView, name='logout'),
]
