from django.contrib.auth.models import User
from django.db import models
from publish.models import Publishable
from django.utils.translation import ugettext_lazy as _


class Article(Publishable):
    title = models.CharField(_('title'), max_length=200)
    subtitle = models.CharField(_('subtitle'), max_length=500, blank=True)
    slug = models.CharField(_('slug'), max_length=100, db_index=True)
    body = models.TextField(_('body'))
    crated_date = models.DateTimeField(auto_now_add=True, editable=False)
    author = models.ForeignKey(User)

    class Meta(Publishable.Meta):
        ordering = ["crated_date"]

    def __unicode__(self):
        return self.title
