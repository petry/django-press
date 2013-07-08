from django.conf.urls import patterns, url
from press.views import ArticleView, SectionView


urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[-_\w]+).html$', ArticleView.as_view(),
        kwargs={'type': 'published'},
        name="press-article-published"),
    url(r'^draft/(?P<slug>[-_\w]+).html$', ArticleView.as_view(),
        kwargs={'type': 'draft'},
        name="press-article-draft"),
    url(r'^section/(?P<slug>[-_\w]+)/$', SectionView.as_view(),
        name="press-section")
)
