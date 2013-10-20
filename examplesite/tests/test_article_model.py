from datetime import datetime
import time
from django.core.urlresolvers import reverse
from django.test import TestCase
from press.models import Article, ArticleSeo
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
        self.assert_field_in('created_date', Article)

    def test_should_have_modified_date(self):
        self.assert_field_in('modified_date', Article)

    def test_should_have_section(self):
        self.assert_field_in('section', Article)

    def test_should_have_user(self):
        self.assert_field_in('user', Article)

    def test_should_output_title_on_model(self):
        article = mommy.make(Article, title='some title')
        self.assertEqual(str(article), article.title)

    def test_should_be_ordered_by_decrescent_date(self):
        fisrt = mommy.make(Article, title='first article')
        time.sleep(2)
        second = mommy.make(Article, title='second article')
        self.assertEqual(Article.objects.all()[0], second)


class SavedArticle(TestCase):
    def setUp(self):
        self.article = mommy.make(Article, title='some title',
                                  subtitle='some subtitle')

    def test_should_have_preview_url_when_article_is_saved(self):
        article_url = reverse('press-article-draft',
                              kwargs={'slug': self.article.slug})
        self.assertEqual(self.article.get_absolute_url(), article_url)

    def test_should_have_published_url_when_article_is_published(self):
        article_url = reverse('press-article-published',
                              kwargs={'slug': self.article.slug})
        self.article.publish()
        published_article = Article.objects.get(Article.Q_PUBLISHED,
                                                slug=self.article.slug)
        self.assertEqual(published_article.get_absolute_url(), article_url)

    def test_should_have_the_same_value_when_it_first_publish(self):
        time.sleep(2)
        self.article.save()
        self.article.publish()
        published_article = Article.objects.get(Article.Q_PUBLISHED,
                                                slug=self.article.slug)
        self.assertEqual(
            datetime.strftime(published_article.created_date, "%H:%M:%S"),
            datetime.strftime(published_article.modified_date, "%H:%M:%S")
        )

    def test_should_get_description_from_article_models_when_not_have_seo_relation(self):
        self.assertEqual(self.article.get_description(), self.article.subtitle)

    def test_should_get_description_from_model_relation(self):
        seo = mommy.make(ArticleSeo, article=self.article, description='meta description')
        self.assertEqual(self.article.get_description(), seo.description)

    def test_should_get_description_from_article_models_when_seo_is_blank(self):
        seo = mommy.make(ArticleSeo, article=self.article)
        self.assertEqual(self.article.get_description(), self.article.subtitle)

    def test_should_not_return_keywords_when_not_have_seo_relation(self):
        self.assertIsNone(self.article.get_keywords())

    def test_should_get_keywords_from_model_relation(self):
        seo = mommy.make(ArticleSeo, article=self.article, keywords='meta keywords')
        self.assertEqual(self.article.get_keywords(), seo.keywords)

    def test_should_not_return_keywords_when_seo_is_blank(self):
        seo = mommy.make(ArticleSeo, article=self.article)
        self.assertIsNone(self.article.get_keywords())

    def test_should_duplicate_seo_atributes(self):
        mommy.make(ArticleSeo, article=self.article, description='meta description')
        self.article.publish()
        draft_article = Article.objects.get(Article.Q_DRAFT,
                                            slug=self.article.slug)
        published_article = Article.objects.get(Article.Q_PUBLISHED,
                                                 slug=self.article.slug)
        self.assertEqual(draft_article.articleseo.description,
                         published_article.articleseo.description)
        self.assertGreater(published_article.articleseo.id,
                           draft_article.articleseo.id)


    def test_should_be_differente_when_it_publish_for_second_time(self):
        self.article.publish()
        draft_article = Article.objects.get(Article.Q_DRAFT,
                                            slug=self.article.slug)
        time.sleep(2)
        draft_article.save()
        draft_article.publish()
        published_article_again = Article.objects.get(Article.Q_PUBLISHED,
                                                      slug=self.article.slug)
        self.assertGreater(
            published_article_again.modified_date,
            published_article_again.created_date
        )
