#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.forms import ModelForm
from django_bleach.forms import BleachField, load_widget
from press.models import Article
from press.settings import PRESS_BLEACH_ALLOWED_TAGS, \
    PRESS_BLEACH_ALLOWED_ATTRIBUTES, \
    PRESS_BLEACH_ALLOWED_STYLES, PRESS_BLEACH_STRIP_TAGS, \
    PRESS_BLEACH_STRIP_COMMENTS, PRESS_DEFAULT_WIDGET


class ArticleAdminForm(ModelForm):
    body = BleachField(
        allowed_tags=PRESS_BLEACH_ALLOWED_TAGS,
        allowed_attributes=PRESS_BLEACH_ALLOWED_ATTRIBUTES,
        allowed_styles=PRESS_BLEACH_ALLOWED_STYLES,
        strip_tags=PRESS_BLEACH_STRIP_TAGS,
        strip_comments=PRESS_BLEACH_STRIP_COMMENTS,
        widget=load_widget(PRESS_DEFAULT_WIDGET)
    )

    class Meta:
        model = Article
