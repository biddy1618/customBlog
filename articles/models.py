from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Article(models.Model):
	title = models.CharField(max_length = 200)
	body = models.TextField()
	pub_date = models.DateField()
	author = models.ForeignKey(User)
	def __str__(self):
		return self.title

class Comment(models.Model):
	body = models.TextField()
	pub_date = models.DateField()
	article = models.ForeignKey(Article)
	author = models.ForeignKey(User)

class Likes(models.Model):
	article = models.ForeignKey(Article)
	author = models.ForeignKey(User)