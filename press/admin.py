from django.contrib import admin
from publish.admin import PublishableAdmin

from press.models import Article


class ArticleAdmin(PublishableAdmin):
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Article, ArticleAdmin)
