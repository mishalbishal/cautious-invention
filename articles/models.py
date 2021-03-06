import uuid

import autoslug
from django.db import models
from django.urls import reverse
from django.utils import timezone
from django_comments.moderation import CommentModerator
from django_comments_xtd.moderation import moderator
import tagulous

from articles.conf import settings


class Author(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    byline = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    author_id = models.IntegerField()  # Used to make url to fool.com

    def __str__(self):
        return self.username


class Image(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)
    created = models.DateTimeField(default=timezone.now)
    modified = models.DateTimeField(null=True, default=timezone.now)

    name = models.CharField(max_length=200, blank=True)
    url = models.URLField()

    featured = models.BooleanField(default=False)


class Article(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    headline = models.CharField(max_length=200, blank=True)
    byline = models.CharField(max_length=100, blank=True)

    body = models.TextField(blank=True)
    pitch = models.TextField(blank=True)
    disclosure = models.TextField(blank=True)
    promo = models.CharField(max_length=200, blank=True)

    # Using default instead of auto_add_now since I'll be loading the articles from a fixture.
    created = models.DateTimeField(default=timezone.now)
    publish_at = models.DateTimeField(default=timezone.now, null=True)
    modified = models.DateTimeField(null=True, default=timezone.now)

    authors = models.ManyToManyField(
        Author, through='AuthorArticle', related_name='articles')

    images = models.ManyToManyField(
        Image, related_name='articles'
    )

    slug = autoslug.AutoSlugField(
        populate_from='headline', unique_with='publish_at', blank=True)

    tags = tagulous.models.TagField()

    # For the scope of this project, I omitted a few things. That I wasn't
    # using like: video, collections, bureau.

    def __str__(self):
        return self.headline

    def get_absolute_url(self):
        return reverse(
            'article-detail',
            kwargs={
                'year': self.publish_at.year,
                'month': int(self.publish_at.strftime('%m').lower()),
                'day': self.publish_at.day,
                'slug': self.slug,
            },
        )


class AuthorArticle(models.Model):
    # Django can create an automatic through table, but having it explicit
    # allows an easier time adding meta-data if necessary in the future.
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)


class ArticleCommentModerator(CommentModerator):
    def moderate(self, comment, content_object, request):
        if settings.ARTICLES_COMMENT_MODERATION_ANONYMOUS:
            return not request.user.is_authenticated
        return super(ArticleCommentModerator, self).moderate(comment, content_object, request)


moderator.register(Article, ArticleCommentModerator)
