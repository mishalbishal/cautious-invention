# Generated by Django 3.1.5 on 2021-01-28 03:57

from django.db import migrations
from django.utils.dateparse import parse_datetime


def add_initial_data(apps, schema_editor):
    Article = apps.get_model('articles', 'Article')
    Author = apps.get_model('articles', 'Author')
    Image = apps.get_model('articles', 'Image')
    from articles import data
    for json in data.get_all_articles():
        article, _ = Article.objects.update_or_create(
            uuid=json['uuid'],
            defaults={
                'uuid': json['uuid'],
                'headline': json['headline'],
                'byline': json['byline'],
                'body': json['body'],
                'pitch': json['pitch'],
                'disclosure': json['disclosure'],
                'promo': json['promo'],
                'created': json['created'],
                # Parsing so that autoslugfield can pick up the datetime obj.
                'publish_at': parse_datetime(json['publish_at']),
                'modified': json['modified'],
            }
        )

        # authors
        authors_list = []
        for author_json in json['authors']:
            author, _ = Author.objects.update_or_create(
                uuid=author_json['uuid'],
                defaults={
                    'uuid': author_json['uuid'],
                    'first_name': author_json['first_name'],
                    'last_name': author_json['last_name'],
                    'byline': author_json['byline'],
                    'username': author_json['username'],
                    'author_id': author_json['author_id'],
                }
            )

            authors_list.append(author)
        article.authors.set(authors_list)

        # images
        image_list = []
        fields = ['uuid', 'name', 'created', 'modified', 'url', 'featured']
        for image_json in json['images']:
            image, _ = Image.objects.update_or_create(
                uuid=image_json['uuid'],
                defaults={field: image_json[field] for field in fields}
            )
            image_list.append(image)
        article.images.set(image_list)

        # tags
        article.tags = [tag['name'] for tag in json['tags']]
        article.save()


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210128_0353'),
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]
