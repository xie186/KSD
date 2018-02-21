import sys, os

## https://stackoverflow.com/questions/39723310/django-standalone-script
import django
sys.path.append(sys.argv[1])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pearDB.settings")
django.setup()

from genewiki_app.models import Gene, Project 

## delete the project
gene = Gene.objects.all()
gene.delete()

print("Gene table: " + sys.argv[2])

with open(sys.argv[2]) as pro:
    for line in pro:
        ## geneid  coordinate  strand best_ara  function_des 
        line = line.rstrip()
        ele = line.split("\t")
        a = Gene(geneid=ele[0], coordinate=ele[1], strand=ele[2],best_ara=ele[3], function_des=ele[4])
        a.save()


