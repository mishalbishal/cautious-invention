from django.shortcuts import render

from . import data
from .models import Article


def index(request):
    # TODO: what if no featured?
    featured = data.get_articles_with_tag('10-promise', limit=1)[0]
    articles = data.get_random_articles(3, exclude=[featured])
    return render(request, 'articles/index.html', {
        'featured': featured,
        'articles': articles,
    })


def detail(request, uuid):
    article = data.get_article(uuid)
    suggested = data.get_random_articles(5, exclude=[article])
    quotes = data.get_random_quotes(3)

    try:
        barticle = Article.objects.get(uuid=article['uuid'])
    except Article.DoesNotExist:
        barticle = Article.objects.create(uuid=article['uuid'])
    # TODO: raise 404 if article not found, either via exception handling or truth checking
    return render(request, 'articles/article.html', {
        'article': article,
        'barticle': barticle,
        'suggested': suggested,
        'quotes': quotes,
    })
