from django.conf.urls import url
from genewiki_app import views

from blastplus import views as blast_view
from blast_app.utils import assign_protein_data_to_blast_results

## API
from rest_framework.urlpatterns import format_suffix_patterns

app_name = 'blast_app'

urlpatterns = [
    # # pearDB url/templates override
    url(r'^blastn/$', blast_view.blastn,
        {'template_init': 'blast.html', 'template_result': 'blast_results.html',
         'extra_context': None}, name = "blastn"),
    url(r'^blastp/$', blast_view.blastp,
        {'template_init': 'blast.html', 'template_result': 'blast_results.html',
         'extra_context': None}, name = "blastp"),
 
]

urlpatterns = format_suffix_patterns(urlpatterns)
