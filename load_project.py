import sys, os

## https://stackoverflow.com/questions/39723310/django-standalone-script
import django
sys.path.append(sys.argv[1])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pearDB.settings")
django.setup()

from django.utils.text import slugify
from genewiki_app.models import Project 

## delete the project
project = Project.objects.all()
project.delete()

print("Project table: " + sys.argv[2])

with open(sys.argv[2]) as pro:
    for line in pro:
        #gene1   GO:00012        BP      Sugur
        line = line.rstrip()
        ele = line.split("\t")
        #https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_one/
        ## gene_obj is query set. List can generate model instances.
        a = Project(title=ele[0], description=ele[1], slug=slugify(ele[0]))
        a.save()


