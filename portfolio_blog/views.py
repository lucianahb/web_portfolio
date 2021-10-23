from django.shortcuts import render
from django.utils import timezone

from .models import PostArticle


def post_article(request):
    post_articles = PostArticle.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'portfolio_blog/post_article.html', {'post_articles': post_articles})
