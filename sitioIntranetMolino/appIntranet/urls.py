from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^loginIntranet$', views.loginIntranet, name='loginIntranet'),
    url(r'^logoutIntranet$', views.logoutIntranet, name='logoutIntranet'),
    url(r'^vales.html$', views.vales, name='vales'),
    # url(r'^errorLogin.html$', views.login, name='errorLogin'),
]