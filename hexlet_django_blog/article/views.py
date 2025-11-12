from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


class IndexArticles(View):
    def get (self, request, article_id=None, tags=None, *args, **kwargs):
        context = {
            "article_id": article_id,
            "tags": tags,
        }
        return render(request,"article/index.html", context)

def redirect_to_article(request):
    # reverse возвращает URL по имени маршрута и аргументам
    url = reverse('article', kwargs={'tags': 'python', 'article_id': 42})
    return redirect(url)
# Create your views here.
