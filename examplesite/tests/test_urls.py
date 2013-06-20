#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.http import Http404
from django.test import TestCase, RequestFactory
from model_mommy import mommy
from press.models import Article
from press.views import ArticleView


class SavedArticle(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('')
        self.view = ArticleView.as_view()
        self.article = mommy.make(Article, title='some title')

    def test_should_have_draft_url_when_article_is_saved(self):
        response = self.view(self.request,
                             slug=self.article.slug, type='draft')
        self.assertEqual(response.status_code, 200)

    def test_should_not_have_published_url_when_article_is_saved(self):
        self.assertRaises(Http404, self.view, self.request,
                          slug=self.article.slug, type='published')

    def test_should_use_article_template(self):
        response = self.view(self.request, slug=self.article.slug,
                             type='draft')
        self.assertTemplateUsed(response, 'press/article_detail.html')


class PublishedArticle(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.request = self.factory.get('')
        self.view = ArticleView.as_view()
        self.article = mommy.make(Article, title='some title')
        self.article.publish()

    def test_should_have_draft_url_when_article_is_saved(self):
        response = self.view(self.request, slug=self.article.slug,
                             type='published')
        self.assertEqual(response.status_code, 200)

    def test_should_use_article_template(self):
        response = self.view(self.request, slug=self.article.slug,
                             type='published')
        self.assertTemplateUsed(response, 'press/article_detail.html')
