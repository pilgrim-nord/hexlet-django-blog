from django import forms  # Импортируем формы Django
from .models import Article
from django.forms import ModelForm


class CommentArticleForm(forms.Form):
    content = forms.CharField(label="Комментарий", max_length=200)


class ArticleForm(ModelForm):
    class Meta:
        model = Article
        fields = ["name", "body"]