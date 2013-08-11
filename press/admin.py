from django.contrib import admin
from django.contrib.admin.options import ModelAdmin
from publish.admin import PublishableAdmin
from press.forms import ArticleAdminForm

from press.models import Article, Author, Section


class ArticleAdmin(PublishableAdmin):
    form = ArticleAdminForm
    prepopulated_fields = {"slug": ("title",)}
    list_display = ['title', 'section', 'publish_state', 'created_date',
                    'modified_date']
    list_filter = ['section', 'publish_state', 'modified_date', 'created_date']
    search_fields = ['title', 'subtitle']

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        super(ArticleAdmin, self).save_model(request, obj, form, change)


class SectionAdmin(ModelAdmin):
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(Author)
admin.site.register(Section, SectionAdmin)
admin.site.register(Article, ArticleAdmin)
