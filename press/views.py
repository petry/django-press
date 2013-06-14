from django.views.generic import DetailView
from press.models import Article


class ArticleView(DetailView):
    queryset = Article.objects.all()