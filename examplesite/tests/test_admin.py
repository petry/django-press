# -*- coding: utf-8 -*-
from django.contrib.auth.models import User
from django.test import TestCase
from django.contrib import admin as django_admin
from django.test.client import RequestFactory
from model_mommy import mommy
from publish.admin import PublishableAdmin
from press.admin import ArticleAdmin
from press.forms import ArticleAdminForm
from press.models import Article, Section


class AdminArticleTest(TestCase):
    def setUp(self):
        self.response = self.client.get('/')

    def test_article_model_should_be_registered_within_the_admin(self):
        self.assertIn(Article, django_admin.site._registry)

    def test_article_admin_must_be_publishabel(self):
        adminClass = django_admin.site._registry[Article]
        self.assertTrue(isinstance(adminClass, PublishableAdmin))

    def test_article_admin_must_have_admin_form(self):
        adminClass = django_admin.site._registry[Article]
        self.assertEqual(adminClass.form, ArticleAdminForm)


class AdminSectionTest(TestCase):
    def test_section_model_should_be_registered_within_the_admin(self):
        self.assertIn(Section, django_admin.site._registry)


class AdminSaveModel(TestCase):
    def setUp(self):
        self.user = User.objects.create_superuser('test', 'test@test.com', 'test')
        self.factory = RequestFactory()
        self.factory.user = self.user

    def test_should_save_the_user_when_use_the_admin(self):
        article = mommy.make(Article)
        article_admin = ArticleAdmin(Article, django_admin)
        article_admin.save_model(
            request=self.factory,
            obj=article,
            form=ArticleAdminForm,
            change=True
        )
        self.assertEqual(article.user, self.user)