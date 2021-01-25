from django.shortcuts import render

from . import data


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
    # TODO: raise 404 if article not found, either via exception handling or truth checking
    return render(request, 'articles/article.html', {
        'article': article,
        'suggested': suggested,
        'quotes': quotes,
    })
