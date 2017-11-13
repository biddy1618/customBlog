from django.shortcuts import render, redirect
from django.contrib import auth
from articles.models import Article, Comment, User, Likes
from django.utils import timezone
from django.http import HttpResponseNotFound, HttpResponse
from forms import ArticleForm, UserForm, MyUserCreationForm, CommentForm
import pdb
# Create your views here.

def articles(request):
	articles = Article.objects.all().order_by('-pub_date')
	return render(
		request,
		'articles.html',
		{
		'articles' : articles,
		'request' : request,
		}
	)

def article(request, article_id):
	article = Article.objects.get(id = article_id)
	if request.user.is_authenticated():
		return render(
			request,
			'article.html',
			{
			'article' : article,
			'request' : request,
			'comments' : Comment.objects.filter(article = article).order_by('-pub_date'),
			'likes' : Likes.objects.filter(article = article).count(),
			'userlike' : Likes.objects.filter(article = article, author = request.user),	
			}
		)
	else:
		return render(
			request,
			'article.html',
			{
			'article' : article,
			'request' : request,
			'comments' : Comment.objects.filter(article = article).order_by('-pub_date'),
			'likes' : Likes.objects.filter(article = article).count(),
			}
		)

def create(request):
	if request.method == 'POST':
		form = ArticleForm(request.POST)
		if form.is_valid():
			article = Article(
				title = form.cleaned_data['title'],
				body = form.cleaned_data['body'],
				pub_date = timezone.now(),
				author = request.user
			)
			article.save()
			return render(
				request,
				'article.html',
				{
				'article' : article,
				'message' : 'You added new article!',
				'request' : request,
				'likes' : Likes.objects.filter(article = article).count(),
				'userlike' : Likes.objects.filter(article = article, author = request.user),	
				}
			)
		else:
			return render(
				request,
				'article_create.html',
				{
				'message' : 'Please, enter valid input!',
				'request' : request,
				}
			)
	return render(
		request,
		'article_create.html',
		{
		'request' : request,
		}
	)

def like(request):
	if request.method == 'POST':
		article = Article.objects.get(id = request.POST['article_id'])
		user = request.user
		if Likes.objects.filter(article = article, author = user).count():
			like = Likes.objects.get(article = article, author = user)
			like.delete()
			return render(
				request,
				'ajax_like.html',
				{
				'likes' : Likes.objects.filter(article = article).count(),
				'userlike' : Likes.objects.filter(article = article, author = request.user),
				}
			)
		else:
			like = Likes(article = article, author = user)
			like.save()
			return render(
				request,
				'ajax_like.html',
				{
				'likes' : Likes.objects.filter(article = article).count(),
				'userlike' : Likes.objects.filter(article = article, author = request.user),
				}
			)


def login(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		user = auth.authenticate(
			username = request.POST['username'],
			password = request.POST['password']
		)
		if user is not None:
			auth.login(request, user)
			return render(
				request,
				'login.html',
				{
				'message' : 'Welcome aboard, %s!' % request.user.username,
				'request' : request,
				}	
			)
		else:
			return render(
				request,
				'login.html',
				{
				'request' : request,
				'message1' : 'Invalid username or password!',
				'message2' : 'Please click ',
				'message3' : ' if you not yet a member.',
				}
			)
	else:
		return render(
			request,
			'login.html',
			{
			'message' : '-Is there life on Mars? -There is no too...',
			'request' : request
			}
		)

def register(request):
	if request.method == 'POST':
		form = MyUserCreationForm(request.POST)
		#pdb.set_trace()
		if form.is_valid():	
			form.save()
			return render(
				request,
				'login.html',
				{
				'message' : 'You are successfully registered. Log in now, please.',
				'request' : request
				}
			)
		else:
			return render(
				request,
				'register.html',
				{
				'message' : 'Please, enter the correct input!',
				'request' : request,
				'form' : form,
				}
			)

def logout(request):
	auth.logout(request)
	return render(
		request,
		'login.html',
		{
		'message' : "You successfully logged out. Can't wait to see you again!",
		'request' : request
		}
	)

def search_titles(request):
	if request.method == 'POST':
		search_text = request.POST['search_text']
	else:
		search_text = ''

	articles = Article.objects.filter(title__contains = search_text)
	return render(
		request,
		'ajax_search.html',
		{
		'articles' : articles,
		}
	)

def add_comment(request):
	if request.method == 'POST':
		form = CommentForm(request.POST)
		if form.is_valid():
			comment = Comment(
				body = form.cleaned_data['body'],
				pub_date = timezone.now(),
				author = request.user,
				article = Article.objects.get(id = form.cleaned_data['article_id']),
			)
			comment.save()
			return render(
				request,
				'ajax_comment.html',
				{
				'comment' : comment
				}
			)

def delete_comment(request):
	if request.method == 'POST':
		comment = Comment.objects.get(id = request.POST['comment_id'])
		comment.delete()
		return render(
			request,
			'ajax_deletecomment.html',
		)

def edit_article(request):
	if request.method =='POST':
		article = Article.objects.get(id = request.POST['article_id'])
		article.title = request.POST['title']
		article.body = request.POST['body']
		article.save()
		return render(
			request,
			'ajax_article.html',
			{
			'article' : article
			}
		)

def delete_article(request):
	if request.method =='POST':
		article = Article.objects.get(id = request.POST['article_id'])
		article.delete()
		return render(
			request,
			'message.html',
			{
			'message' : 'You successfully deleted article'
			}
		)

