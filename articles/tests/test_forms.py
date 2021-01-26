from django.test import TestCase
from django_comments_xtd import django_comments

from articles import forms
from articles.models import Article


class EmailOptionalFormTest(TestCase):
    def test_email_field_is_optional(self):
        article = Article.objects.create()
        form = django_comments.get_form()(article)
        print(form)
        self.assertFalse(form.fields['email'].required)
