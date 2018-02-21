import sys, os
import os

## https://stackoverflow.com/questions/39723310/django-standalone-script
import django
sys.path.append(sys.argv[1])
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pearDB.settings")
django.setup()

from genewiki_app.models import Gene, GO

print("Gene table: " + sys.argv[2])
print("GO table: " + sys.argv[3])

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

go = GO.objects.all()
go.delete()

with open(sys.argv[3]) as go:
    for line in go:
        #gene1   GO:00012        BP      Sugur
        line = line.rstrip()
        ele = line.split("\t")
        #pk_gene = gene_dict[ele[0]]
        gene_obj = Gene.objects.all().filter(pk=ele[0])
        print(gene_obj)
        #https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_one/
        ## gene_obj is query set. List can generate model instances. 
        a = GO(accession=ele[1], namespace=ele[2], description=ele[3], gene=list(gene_obj)[0])
        a.save()
