from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone
from publish.models import Publishable
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse as reverse_url

class Author(models.Model):
    user = models.ForeignKey(User, verbose_name=_('user'))
    about = models.TextField(_('about'))

    class Meta(Publishable.Meta):
        ordering = ["user__first_name", "user__last_name"]

    def __unicode__(self):
        return self.user.get_full_name()


class Article(Publishable):
    title = models.CharField(_('title'), max_length=200)
    slug = models.CharField(_('slug'), max_length=100, db_index=True)
    subtitle = models.CharField(_('subtitle'), max_length=500, blank=True)
    body = models.TextField(_('body'))
    created_date = models.DateTimeField(_('created date'), auto_now_add=True, editable=False, default=timezone.now())
    modified_date = models.DateTimeField(_('modified date'), auto_now=True, editable=False, default=timezone.now())
    user = models.ForeignKey(User, verbose_name=_('user'), editable=False)
    author = models.ForeignKey(Author, blank=True, null=True)

    class Meta(Publishable.Meta):
        ordering = ["modified_date"]

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        if self.is_public:
            return reverse_url('press-article-published', args=[self.slug])
        return reverse_url('press-article-draft', args=[self.slug])