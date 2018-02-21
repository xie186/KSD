import sys, os
from genewiki_app.models import Gene, GO

print("Gene table: " + sys.argv[1])
print("GO table: " + sys.argv[2])

## https://docs.djangoproject.com/en/2.0/topics/db/examples/many_to_one/
gene_dict = dict()
with open(sys.argv[1]) as tab:
    i = 1
    for line in tab:
        line = line.rstrip()
        ele = line.split("\t")
        gene_dict[ele[0]] = i
        i = i +1

#print(gene_dict)

with open(sys.argv[2]) as go:
    for line in go:
        #gene1   GO:00012        BP      Sugur
        line = line.rstrip()
        ele = line.split("\t")
        pk_gene = gene_dict[ele[0]]
        gene_obj = Gene.objects.all.filter(pk=pk_gene)
        print(gene_obj)
        
        

