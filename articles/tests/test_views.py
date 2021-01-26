import uuid
from unittest import skip

from django.test import TestCase
from django.urls import reverse
# from django.contrib.staticfiles.testing import StaticLiveServerTestCase
# from selenium.webdriver.firefox.webdriver import WebDriver


class IndexViewTest(TestCase):
    @skip
    def test_uses_correct_template(self):
        response = self.client.get(reverse('index'))

        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check we used correct template
        self.assertTemplateUsed(response, 'articles/index.html')


# class IndexViewSeleniumTest(StaticLiveServerTestCase):
#     @classmethod
#     def setUpClass(cls):
#         super().setUpClass()
#         cls.selenium = WebDriver()
#         cls.selenium.implicitly_wait(10)

#     @classmethod
#     def tearDownClass(cls):
#         cls.selenium.quit()
#         super().tearDownClass()

#     # Make this a selenium testscase.
#     def test_view_has_correct_title(self):
#         self.selenium.get('%s%s' % (self.live_server_url, '/'))
#         title_element = self.selenium.find_element_by_tag_name("title")
#         self.assertEquals(
#             title_element.get_attribute("value"),
#             "Homepage",
#         )
#     # Make this a selenium testscase.

#     @skip
#     def test_correct_url_for_featured_image(self):
#         pass
#         # ??
#     # Make this a selenium testscase.

#     @skip
#     def test_fallback_if_no_featured(self):
#         pass


class ArticleDetailViewTest(TestCase):
    def test_uses_correct_template(self):
        response = self.client.get(
            reverse('article-detail', args=[uuid.uuid4()])
        )
        # Check that we got a response "success"
        self.assertEqual(response.status_code, 200)
        # Check we used correct template
        self.assertTemplateUsed(response, 'articles/article.html')

    @skip   # Until the view uses get_object_or_404.
    def test_non_existent_article(self):
        response = self.client.get(
            reverse('article-detail', args=[uuid.uuid4()])
        )
        self.assertEqual(response.status_code, 404)

    # Make this a selenium test case since we're testing the rendered html.
    @skip
    def test_contains_comment_form(self):
        article = data.get_random_articles(1)[0]
        arg = article['uuid']
        response = self.client.get(reverse('article-detail', args=[arg]))
        self.assertContains(response, 'TimerX')

    # Make this a selenium testscase.
    @skip
    def test_view_has_correct_title(self):
        # response = self.client.get(reverse('article-detail'))
        # self.assertContains(response, "<title>{}</title>".format("Homepage"))
        pass

    # Make this a selenium testscase.
    @skip
    def test_shuffle_button_components(self):
        pass
        # Ensure button exists and relevant javascript also exists.
