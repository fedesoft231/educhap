from django.conf.urls import url
from apieduchap import views
urlpatterns = [

 url(r'^universidad/$', views.UniversidadList.as_view()),
 url(r'^universidad/(?P<pk>[0-9]+)/$', views.UniversidadDetail.as_view()),

 url(r'^carrera/$', views.CarreraList.as_view()),
 url(r'^carrera/(?P<pk>[0-9]+)/$', views.CarreraDetail.as_view()),

 url(r'^usuarios/$', views.UsuarioList.as_view()),
 url(r'^usuarios/(?P<pk>[0-9]+)/$', views.UsuarioDetail.as_view()),
 
]