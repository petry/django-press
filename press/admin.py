from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from publish.admin import PublishableAdmin, PublishableTabularInline, PublishableStackedInline
from publish.admin import Publishable
from press.forms import ArticleAdminForm

from press.models import Article, Section, ArticleSeo




class ArticleSeoInline(PublishableStackedInline):
    model = ArticleSeo


class ArticleAdmin(PublishableAdmin):
    form = ArticleAdminForm
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'section', 'publish_state', 'created_date',
                    'modified_date']
    list_filter = ['section', 'publish_state', 'modified_date', 'created_date']
    search_fields = ['title', 'subtitle']
    inlines = [
        ArticleSeoInline
    ]

    class PublishMeta(Publishable.PublishMeta):
        publish_reverse_fields = [
            'articleseo'
        ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ArticleAdmin, self).save_model(request, obj, form, change)


class SectionAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Section, SectionAdmin)
admin.site.register(Article, ArticleAdmin)

