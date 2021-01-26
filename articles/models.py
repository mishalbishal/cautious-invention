import uuid

from django.db import models
from django.urls import reverse
from django_comments.moderation import CommentModerator
from django_comments_xtd.moderation import moderator


class Article(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'uuid': self.uuid})


class ArticleCommentModerator(CommentModerator):
    def moderate(self, comment, content_object, request):
        if not request.user.is_authenticated:
            return True
        return super(ArticleCommentModerator, self).moderate(comment, content_object, request)


moderator.register(Article, ArticleCommentModerator)
