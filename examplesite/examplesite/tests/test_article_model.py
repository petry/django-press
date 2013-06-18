from django.core.urlresolvers import reverse
from django.test import TestCase
from press.models import Article
from model_mommy import mommy


class ArticleModelTestCase(TestCase):
    def assert_field_in(self, field_name, model):
        self.assertIn(field_name, model._meta.get_all_field_names())

    def test_should_have_title(self):
        self.assert_field_in('title', Article)

    def test_should_have_subtitle(self):
        self.assert_field_in('subtitle', Article)

    def test_should_have_slug(self):
        self.assert_field_in('slug', Article)

    def test_should_have_body(self):
        self.assert_field_in('body', Article)

    def test_should_have_crated_date(self):
        self.assert_field_in('crated_date', Article)

    def test_should_have_author(self):
        self.assert_field_in('author', Article)

    def test_should_output_title_on_model(self):
        article = mommy.make(Article, title='some title')
        self.assertEqual(str(article), article.title)

class SavedArticle(TestCase):
    def setUp(self):
        self.article = mommy.make(Article, title='some title')

    def test_should_have_preview_url_when_article_is_saved(self):
        article_url = reverse('press-article-draft', kwargs={'slug':self.article.slug})
        self.assertEqual(self.article.get_absolute_url(), article_url)

    def test_should_have_published_url_when_article_is_saved(self):
        article_url = reverse('press-article-published', kwargs={'slug':self.article.slug})
        self.article.publish()
        published_article = Article.objects.get(Article.Q_PUBLISHED, slug=self.article.slug)
        self.assertEqual(published_article.get_absolute_url(), article_url)

