import uuid

from django.db import models
from django.urls import reverse


class Article(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def get_absolute_url(self):
        return reverse('article-detail', kwargs={'uuid': self.uuid})