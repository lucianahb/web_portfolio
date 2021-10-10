from django.shortcuts import render


def post_article(request):
    return render(request, 'portfolio_blog/post_article.html', {})
