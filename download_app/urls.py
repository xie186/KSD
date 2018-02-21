from django.conf.urls import url
from download_app import views

## API
#from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'download_app'

urlpatterns = [
    ## API
    #url(r'^api/expdb/$', views.ExpDBList.as_view(), name="expdbAPI"),
    #url(r'^api/expdb/(?P<geneid>.*)/(?P<pro_slug>.*)/$', views.ExpDBGenePro.as_view(), name="expdbGeneProAPI"),
    #url(r'^api/expdb/(?P<geneid>.*)/$', views.ExpDBListGene.as_view(), name="expdbGeneAPI"),
    ## Download list
    url(r'^download/$', views.DownloadFileList.as_view(), name='downloadfile'),
    url(r'^download/(?P<slug>.*)/$', views.download_data_package, name='downloaddata'),
    #url(r'^(?P<pk>.*)/$', views.GeneDetailView.as_view(), name='genelist'),
]

#urlpatterns = format_suffix_patterns(urlpatterns)

