from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from publish.models import Publishable
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse as reverse_url


class Article(Publishable):
    title = models.CharField(_('title'), max_length=200)
    slug = models.CharField(_('slug'), max_length=100, db_index=True)
    subtitle = models.CharField(_('subtitle'), max_length=500, blank=True)
    body = models.TextField(_('body'))
    created_date = models.DateTimeField(auto_now_add=True, editable=False, default=timezone.now())
    modified_date = models.DateTimeField(auto_now=True, editable=False, default=timezone.now())
    author = models.ForeignKey(User)

    class Meta(Publishable.Meta):
        ordering = ["created_date"]

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        if self.is_public:
            return reverse_url('press-article-published', args=[self.slug])
        return reverse_url('press-article-draft', args=[self.slug])