from django.views.generic import DetailView
from press.models import Article


class ArticleView(DetailView):

    def get_queryset(self):
        queryset_by_type = {
            'draft': Article.Q_DRAFT,
            'published': Article.Q_PUBLISHED
        }
        return Article.objects.filter(queryset_by_type[self.kwargs['type']])
