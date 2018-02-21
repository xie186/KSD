from django.conf.urls import url, include
from genewiki_app import views
import haystack

## API
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'genewiki_app'

urlpatterns = [
    ## API
    url(r'^api/expdb/$', views.ExpDBList.as_view(), name="expdbAPI"),
    url(r'^api/expdb/(?P<geneid>.*)/(?P<pro_slug>.*)/$', views.ExpDBGenePro.as_view(), name="expdbGeneProAPI"),
    url(r'^api/expdb/(?P<geneid>.*)/$', views.ExpDBListGene.as_view(), name="expdbGeneAPI"),
    ## gene list
    ## in haystack.urls is named as 'haystack_search'
    ## https://github.com/django-haystack/django-haystack/blob/master/haystack/urls.py
    url(r'^search/', include('haystack.urls')),
    url(r'^(?P<pk>.*)/$', views.GeneDetailView.as_view(), name='genelist'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
