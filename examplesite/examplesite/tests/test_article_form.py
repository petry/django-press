#!/usr/bin/env python
# -*- coding: utf-8 -*-
from ckeditor.widgets import CKEditorWidget
from django.test import TestCase
from press.forms import ArticleAdminForm
from press.settings import PRESS_BLEACH_ALLOWED_ATTRIBUTES, \
    PRESS_BLEACH_ALLOWED_STYLES, PRESS_BLEACH_STRIP_TAGS, \
    PRESS_BLEACH_STRIP_COMMENTS, PRESS_BLEACH_ALLOWED_TAGS


class FormArticleTest(TestCase):

    def setUp(self):
        super(FormArticleTest, self).setUp()
        form = ArticleAdminForm()
        self.body_field = form.fields['body']

    def test_should_use_press_widget(self):
        self.assertIsInstance(self.body_field.widget, CKEditorWidget)

    def test_form_should_use_bleach_configuration(self):
        self.assertEqual(self.body_field.bleach_options['styles'],
                         PRESS_BLEACH_ALLOWED_STYLES)
        self.assertEqual(self.body_field.bleach_options['attributes'],
                         PRESS_BLEACH_ALLOWED_ATTRIBUTES)
        self.assertEqual(self.body_field.bleach_options['strip'],
                         PRESS_BLEACH_STRIP_TAGS)
        self.assertEqual(self.body_field.bleach_options['strip_comments'],
                         PRESS_BLEACH_STRIP_COMMENTS)
        self.assertEqual(self.body_field.bleach_options['tags'],
                         PRESS_BLEACH_ALLOWED_TAGS)
