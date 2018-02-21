"""KSD URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from basic_app import views as basic_views
from genewiki_app import views as genewiki_views
from download_app import views as download_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blast/', include('blastplus.urls')),
    url(r'^$',basic_views.IndexView.as_view(), name="home"),
    url(r'^genewiki_app/',include('genewiki_app.urls',namespace='genewiki_app')),
    url(r'^blast_app/',include('blast_app.urls',namespace='blast_app')),
    url(r'^download_app/',include('download_app.urls',namespace='download_app')),
    #url(r'^$',basic_views.IndexView.as_view(), name="home"),
]
