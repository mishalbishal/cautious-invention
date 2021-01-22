# Putting the dump of content_api.json and quotes_api.json into a relational database seems like a large task.
# It also happens to *not exactly* be in the scope of the project. So, I'm going to mock out database access
# for now and come back if time allows.
# The benefit of owning the data in a database is that it is easier to work with using Django's ORM.
# It would also enable building out features such as using the admin site to allow authors to write new articles.
# The cons are that implementing actual search with tags requires a lot of code.

import json
import functools
import random


@functools.cache
def get_content_api(filename='data/content_api.json'):
    with open(filename, 'rb') as f:
        data = json.load(f)
        return data
    # TODO: what's the default here? Should be an exception but whichone?
    raise RuntimeError("API data file not found.")


def get_random_articles(limit):
    data = get_content_api()
    articles = data.get('results', [])
    return random.sample(articles, limit)


def get_article(uuid):
    # The json load is just a string, whereas flask uses as python uuid object, so just convert to a string
    # for this example.
    uuid = str(uuid)
    data = get_content_api()
    for article in data['results']:
        if article['uuid'] == uuid:
            return article
    raise LookupError("Article with uuid: {} not found".format(uuid))


def get_articles_with_tag(tag, limit=10):
    data = get_content_api()
    res = []
    for article in data['results']:
        if any(tag == x['slug'] for x in article['tags']):
            res.append(article)
    return res[:limit]
