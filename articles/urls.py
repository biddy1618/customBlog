from django.conf.urls import patterns, url
from articles import views

urlpatterns = patterns('',
	url(r'^$', views.articles, name = 'articles'),
	url(r'^get/(?P<article_id>\d+)/$', views.article, name = 'article'),
	url(r'^create/$', views.create, name = 'create'),
	url(r'^like/$', views.like, name = 'like'),
	#url(r'^add_comment/(?P<article_id>\d+)/$', views.add_comment, name = 'add_comment'),
	#url(r'^delete_comment/(?P<comment_id>\d+)/$', views.delete_comment, name = 'delete_comment'),
	url(r'^accounts/login/$', views.login, name = 'login'),
	#url(r'^accounts/auth/$', views.auth_view, name = 'auth'),
	url(r'^accounts/logout/$', views.logout, name = 'logout'),
	#url(r'^accounts/loggedin/$', views.loggedin, name = 'loggedin'),
	#url(r'^accounts/invalid/$', views.invalid_login, name = 'invalid'),
	url(r'^accounts/register/$', views.register, name = 'register'),
	#url(r'^accounts/register_success/$', views.register_success, name = 'register_success'),
	url(r'^search/$', views.search_titles, name = 'search'),
	url(r'^add_comment/$', views.add_comment, name = 'add_comment'),
	url(r'^delete_comment/$', views.delete_comment, name = 'delete_comment'),
	url(r'^edit_article/$', views.edit_article, name = 'edit_article'),
	url(r'^delete_article/$', views.delete_article, name = 'delete')
)