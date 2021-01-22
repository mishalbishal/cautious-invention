from django.shortcuts import render

from . import data


def index(request):
    # TODO: what if no featured?
    featured = data.get_articles_with_tag('10-promise', limit=1)[0]
    print(featured)
    articles = data.get_random_articles(3)
    return render(request, 'articles/index.html', {
        'featured': featured,
        'articles': articles,
    })


def detail(request, uuid):
    return render(request, 'articles/article.html')
