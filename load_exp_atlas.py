import sys, os
import os

## https://stackoverflow.com/questions/39723310/django-standalone-script
import django
sys.path.append(sys.argv[1])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pearDB.settings")
django.setup()

from genewiki_app.models import Gene, ExpDB

print("Gene table: " + sys.argv[2])
print("Gene expression table: " + sys.argv[3])

## https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_one/
gene_dict = dict()
with open(sys.argv[2]) as tab:
    i = 1
    for line in tab:
        line = line.rstrip()
        ele = line.split("\t")
        gene_dict[ele[0]] = i
        i = i +1

#print(gene_dict)

expdb = ExpDB.objects.all()
expdb.delete()

with open(sys.argv[3]) as expdb:
    for line in expdb:
        line = line.rstrip()
        ele = line.split("\t")  ## project gene sample fpkm
        #pk_gene = gene_dict[ele[1]]
        gene_obj = Gene.objects.all().filter(pk=ele[1])
        #https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_one/
        ## gene_obj is query set. List can generate model instances. 
        a = ExpDB(project=ele[0], gene=list(gene_obj)[0], sample=ele[2], fpkm=ele[3])
        a.save()
