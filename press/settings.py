#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.conf import settings

PRESS_DEFAULT_WIDGET = getattr(settings, "PRESS_DEFAULT_WIDGET",
                               'django.forms.Textarea')

PRESS_BLEACH_ALLOWED_TAGS = getattr(settings, "PRESS_BLEACH_ALLOWED_TAGS", [
    'h1', 'h2', 'h3', 'h4', 'h5', 'h6',
    'p', 'ul', 'ol', 'li',
    'br', 'hr', 'blockquote',
    'strong', 'em', 'u', 'strike', 'a',
    'table', 'tr', 'th', 'td', 'tbody', 'caption',
    'img', 'h1'
])

PRESS_BLEACH_ALLOWED_ATTRIBUTES = getattr(settings,
                                          "PRESS_BLEACH_ALLOWED_ATTRIBUTES", {
        'a': [
            'href', 'target',
            'class', 'id', 'name', 'style', 'title',
        ],
        'p': [
            'style'
        ],
        'img': [
            'src', 'width', 'height', 'alt', 'title', 'id', 'style'
        ],
        'table': [
            'border', 'cellpadding', 'cellspacing', 'style', 'summary',
            'width', 'height', 'align'
        ]
    })
PRESS_BLEACH_ALLOWED_STYLES = getattr(settings,
                                      "PRESS_BLEACH_ALLOWED_STYLES", [])
PRESS_BLEACH_STRIP_TAGS = getattr(settings, "PRESS_BLEACH_STRIP_TAGS", True)
PRESS_BLEACH_STRIP_COMMENTS = getattr(settings, "PRESS_BLEACH_STRIP_COMMENTS",
                                      True)