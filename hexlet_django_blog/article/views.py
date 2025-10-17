from django.shortcuts import render

def index(request):

    return render(
        request,
        "article/index.html",
        context={
            "app_name": "hexlet_django_blog.article",
        }
    )

# Create your views here.
