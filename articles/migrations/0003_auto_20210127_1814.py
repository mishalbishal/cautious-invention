# Generated by Django 3.1.5 on 2021-01-27 18:14

from django.db import migrations


def add_initial_data(apps, schema_editor):
    Article = apps.get_model('articles', 'Article')
    Author = apps.get_model('articles', 'Author')
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
                'publish_at': json['publish_at'],
                'modified': json['modified'],
            }
        )
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


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0002_auto_20210127_1814'),
    ]

    operations = [
        migrations.RunPython(add_initial_data),
    ]