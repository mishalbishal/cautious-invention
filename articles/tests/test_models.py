from django.test import TestCase
from django.utils import timezone

from articles.models import Article, Author


class ArticleReadonlyTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        author = Author.objects.create(
            first_name='Test',
            last_name='User',
            byline='Test User',
            username='TMFtestuser',
            author_id=42,
        )
        article = Article.objects.create(
            headline='Article title',
        )
        article2 = Article.objects.create(
            headline='Article title',
        )
        article.authors.set([author])

    def test_article_representation(self):
        article = Article.objects.all()[0]
        self.assertEquals(str(article), article.headline)

    def test_absolute_url(self):
        article = Article.objects.all()[0]
        url = '/articles/{}/{}/{}/{}'.format(
            article.publish_at.year,
            int(article.publish_at.strftime('%m').lower()),
            article.publish_at.day,
            article.slug
        )
        self.assertEquals(article.get_absolute_url(), url)

    def test_unique_slugs_for_same_title(self):
        articles = Article.objects.filter(headline='Article title').all()
        slugs = [article.slug for article in articles]
        headlines = [article.headline for article in articles]

        self.assertEquals(len(slugs), 2)
        self.assertEquals(len(set(slugs)), 2)

        self.assertEquals(len(headlines), 2)
        self.assertEquals(len(set(headlines)), 1)
