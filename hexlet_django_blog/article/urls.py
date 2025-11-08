from django.urls import path

from hexlet_django_blog.article import views
from hexlet_django_blog.article.views import IndexArticles

urlpatterns = [
    path("", IndexArticles.as_view(), name="article_index"),
]
