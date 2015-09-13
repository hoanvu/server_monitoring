from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.IndexView.as_view(), name='index'),
	url(r'^userLogin/$', views.userLogin, name='userLogin'),
	url(r'^userLogout/$', views.userLogout, name='userLogout'),
	url(r'^addServer/$', views.addServer, name='addServer'),
	url(r'^removeServer/([0-9]+)/$', views.removeServer, name='removeServer'),
	url(r'^allUser/$', views.allUser, name='allUser'),
	url(r'^addUser/$', views.addUser, name='addUser'),
	url(r'^removeUser/([\w\d]+)/$', views.removeUser, name='removeUser'),
]