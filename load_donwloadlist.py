import sys, os

## https://stackoverflow.com/questions/39723310/django-standalone-script
import django
sys.path.append(sys.argv[1])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pearDB.settings")
django.setup()

from django.utils.text import slugify
from download_app.models import DownloadFile 

## delete the project
project = DownloadFile.objects.all()
project.delete()

print("DownloadFile table: " + sys.argv[2])

with open(sys.argv[2]) as pro:
    for line in pro:
        #project-detail  project_detail.tab.gz   all the details about project 
        line = line.rstrip()
        ele = line.split("\t")
        #https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_one/
        ## gene_obj is query set. List can generate model instances.
        a = DownloadFile(name=ele[1], description=ele[2], slug=slugify(ele[0]))
        a.save()


