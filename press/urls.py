from django.conf.urls import patterns, url
from press.views import ArticleView


urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[-_\w]+).html$', ArticleView.as_view(),
        kwargs={'type': 'published'},
        name="press-article-published"),
    url(r'^draft/(?P<slug>[-_\w]+).html$', ArticleView.as_view(),
        kwargs={'type': 'draft'},
        name="press-article-draft"),
)
