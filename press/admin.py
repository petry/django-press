from django.contrib import admin
from publish.admin import PublishableAdmin

from press.models import Article, Author


class ArticleAdmin(PublishableAdmin):
    prepopulated_fields = {"slug": ("title",)}

    def save_model(self, request, obj, form, change):
        if not change:
            obj.user = request.user
        super(ArticleAdmin, self).save_model(request, obj, form, change)


admin.site.register(Author)
admin.site.register(Article, ArticleAdmin)
