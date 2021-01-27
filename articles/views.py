from django.shortcuts import render, redirect, get_object_or_404

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
    article = get_object_or_404(Article, uuid=uuid)
    qs = Article.objects.exclude(uuid=uuid)

    # Ordering by ? is expensive. But it's fine for 10 articles.
    # I wouldn't do this in production, but keeping it here
    # and listing alternatives:
    # * Use postgres' tablesample to get approximate random articles.
    # * Use an autoincrement id field, then choose a random sample in range (1, last_autoincrement_id).
    qs = qs.order_by('?')
    suggested = qs.all()[:3]
    quotes = data.get_random_quotes(3)

    return render(request, 'articles/article.html', {
        'article': article,
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


def hotlink_author_profile(request, author_id):
    template = "https://www.fool.com/author/{}/"
    return redirect(template.format(author_id))
