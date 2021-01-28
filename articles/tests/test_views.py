import uuid
from unittest import skip

from django.test import TestCase
from django.urls import reverse

from articles.models import Article, Author


class IndexViewTest(TestCase):
    def test_uses_correct_template(self):
        response = self.client.get(reverse('index'))

        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check we used correct template
        self.assertTemplateUsed(response, 'articles/index.html')

    # Should be a selenium test.
    def test_view_has_correct_title(self):
        response = self.client.get(reverse('index'))
        self.assertContains(response, "<title>{}</title>".format("Homepage"))


class ArticleDetailViewTest(TestCase):
    def setUp(self):
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
        article.authors.set([author])

    def test_uses_correct_template(self):
        article = Article.objects.filter(headline='Article title').all()[0]
        response = self.client.get(
            article.get_absolute_url()
        )
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check we used correct template
        self.assertTemplateUsed(response, 'articles/article.html')

    def test_non_existent_article(self):
        article = Article.objects.filter(headline='Article title').all()[0]
        article.delete()
        response = self.client.get(article.get_absolute_url())
        self.assertEqual(response.status_code, 404)

    # Should be a selenium test.
    def test_view_has_correct_title(self):
        article = Article.objects.filter(headline='Article title').all()[0]
        response = self.client.get(article.get_absolute_url())
        self.assertContains(
            response,
            "<title>{}</title>".format(article.headline),
        )
