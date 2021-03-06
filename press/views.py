from django.views.generic import DetailView
from django.views.generic.list import ListView
from press.models import Article


class ArticleView(DetailView):


    def get(self, request, *args, **kwargs):
        return super(ArticleView, self).get(request, *args, **kwargs)

    def get_queryset(self):
        queryset_by_type = {
            'draft': Article.Q_DRAFT,
            'published': Article.Q_PUBLISHED
        }
        return Article.objects.filter(queryset_by_type[self.kwargs['type']])


class SectionView(ListView):
    model = Article
