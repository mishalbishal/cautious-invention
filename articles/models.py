import uuid

from django.db import models

# Create your models here.


class Article(models.Model):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

