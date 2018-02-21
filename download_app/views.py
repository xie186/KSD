import os
from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from download_app.models import DownloadFile

from django.http import StreamingHttpResponse
from django.core.files import File

from pearDB.settings import DOWNLOAD_DIR 

class DownloadFileList(ListView):
    model = DownloadFile

def download_data_package(request, slug):
    """ Generic download method for compressed data.
        Download snippet source https://djangosnippets.org/snippets/365/
    """

    assert request.method == 'GET'
    #slug = request.GET.get('slug')
    downloadfile = list(DownloadFile.objects.filter(slug=slug))[0]
    
    out_file_name = downloadfile.name
    file_path = os.path.join(DOWNLOAD_DIR, downloadfile.name)
    wrapper = File(file(file_path))
     
    response = StreamingHttpResponse(wrapper, content_type="application/gz")
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(out_file_name)
    return response
