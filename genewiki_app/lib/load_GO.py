import sys
from genewiki_app.models import Gene, GO

print("Gene table: " + sys.argv[1])
print("GO table: " + sys.argv[2])

gene_dict = dict()
with open(sys.argv[1]) as tab:
    i = 1
    for line in tab:
        line = line.rstrip()
        ele = line.split("\t")
        gene_dict[ele[0]] = i
        i = i +1


