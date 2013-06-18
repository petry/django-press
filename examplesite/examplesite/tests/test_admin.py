# -*- coding: utf-8 -*-
from django.test import TestCase, RequestFactory
from django.contrib import admin as django_admin
from publish.admin import PublishableAdmin
from press.models import Article, Author


class AdminArticleTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_article_model_should_be_registered_within_the_admin(self):
        self.assertIn(Article, django_admin.site._registry)

    def test_article_admin_must_be_publishabel(self):
        adminClass = django_admin.site._registry[Article]
        self.assertTrue(isinstance(adminClass, PublishableAdmin))

class AdminAuthorTest(TestCase):
    def test_author_model_should_be_registered_within_the_admin(self):
        self.assertIn(Author, django_admin.site._registry)
