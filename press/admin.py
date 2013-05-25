from django.contrib import admin
from publish.admin import PublishableAdmin

from press.models import Article


class ArticleAdmin(PublishableAdmin):
    pass

admin.site.register(Article, ArticleAdmin)