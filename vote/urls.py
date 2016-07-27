from django.conf.urls import url
from vote import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/(?P<state_id>[A-Za-z]{2})/$', views.register, name='register_state'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^account/$', views.account, name='account'),
    url(r'^states/$', views.states, name='states'),
]