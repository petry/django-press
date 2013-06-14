from django.conf.urls import patterns, url
from press.views import ArticleView


urlpatterns = patterns(
    '',
    url(r'^(?P<slug>[-_\w]+).html$', ArticleView.as_view(), name="press-article-detail"),
)
