from django import forms
from models import Article, Comment
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm



class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = {'title', 'body'}

class CommentForm(forms.ModelForm):
	article_id = forms.CharField()

	class Meta:
		model = Comment
		fields = {'body', 'article_id'}

class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = {'username', 'password'}

class MyUserCreationForm(UserCreationForm):
	email = forms.EmailField(required = True)

	class Meta:
		model = User
		fields = {'username', 'email', 'password1', 'password2'}

	def save(self, commit = True):
		user = super(MyUserCreationForm, self).save(commit = False)
		user.email = self.cleaned_data['email']

		if commit:
			user.save()

		return user

