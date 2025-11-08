from django.shortcuts import render
from django.views import View


class IndexArticles(View):
    def get (self, request, *args, **kwargs):
        context = {
            "app_name": "hexlet_django_blog.article",}
        return render(request,"article/index.html", context)


# Create your views here.
