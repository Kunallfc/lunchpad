from django.conf.urls import url,include
import views

urlpatterns=[
	url(r'^$', views.welcome),
	url(r'^signin', views.register_data),
    url(r'^login', views.login_data),
    url(r'^log', views.loggin),    
    url(r'^register', views.register),
    url(r'^profile', views.profile),
    url(r'^search', views.search),
    url(r'^home', views.home),
]
