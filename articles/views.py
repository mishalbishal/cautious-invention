from django.shortcuts import render, redirect

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

def logo_image(request, symbol):
    # Offloading finding the correct company logo image to the fool's image cdn.
    # Doing it via a view in case I want to change this later.
    # Possible changes:
    # * Add caching in front of the fool image cdn.
    # * Handle 404s, by having a placeholder image.
    template = "https://g.foolcdn.com/image/?url=https%3A%2F%2Fg.foolcdn.com%2Fart%2Fcompanylogos%2Fmark%2F{}.png&w=64&h=64&op=resize"
    url = template.format(symbol)
    return redirect(url)
