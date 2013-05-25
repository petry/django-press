# -*- coding: utf-8 -*-
from django.test import TestCase
from django.contrib import admin as django_admin
from press.models import Article


class AdminArticleTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_article_model_should_be_registered_within_the_admin(self):
        self.assertIn(Article, django_admin.site._registry)
