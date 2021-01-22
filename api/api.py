from flask import Flask, jsonify
import json
import functools

debug = True
app = Flask(__name__)

content_api = None
quotes_api = None


@functools.cache
def get_content_api(filename='data/content_api.json'):
    with open(filename, 'rb') as f:
        data = json.load(f)
        return data
    # TODO: what's the default here? Should be an exception but whichone?
    raise RuntimeError("API data file not found.")


@app.route('/articles/<uuid:uuid>/')
def get_article(uuid):
    # The json load is just a string, whereas flask uses as python uuid object, so just convert to a string
    # for this example.
    uuid = str(uuid)
    data = get_content_api()
    print("Results: ", data['results'])
    for article in data['results']:
        if article['uuid'] == uuid:
            return article
    raise LookupError("Article with uuid: {} not found".format(uuid))


@app.route('/articles/tag/<string:tag>/')
def get_article_tag(tag):
    data = get_content_api()
    res = []
    for article in data['results']:
        if any(tag == x['slug'] for x in article['tags']):
            res.append(article)

    return jsonify({'results': res})


@app.route('/articles')
def get_all_articles():
    return get_content_api()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=debug)
