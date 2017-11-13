from django.contrib import admin
from articles.models import Article, Comment, Likes

# Register your models here.
admin.site.register(Article)
admin.site.register(Comment)
admin.site.register(Likes)
