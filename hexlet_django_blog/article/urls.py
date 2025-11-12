from django.urls import path

from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexArticles, redirect_to_article

urlpatterns = [
    path("", redirect_to_article, name='index'),
    path("<str:tags>/<int:article_id>", IndexArticles.as_view(), name="article"),
]
