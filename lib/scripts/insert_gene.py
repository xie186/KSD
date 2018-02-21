import sqlite3
import sys
print("Input data: ")
print("Database file: " + sys.argv[1])
print("Tables: " + sys.argv[2])
print("Tab file: " + sys.argv[3])

conn = sqlite3.connect(sys.argv[1])
c = conn.cursor()

index = 1
with open(sys.argv[3]) as tab:
    for line in tab:
        line = line.rstrip()
        #gene1   chr1:3000-4000  +       Ara01   CBF
        #gene_id, coor, strand, best_ara, gene_des
        line_array = line.split("\t")
        print(line_array)
        cmd = "INSERT INTO {tab} VALUES ({index},'{gene_id}', '{coor}', '{strand}', '{best_ara}', '{gene_des}')".format(tab=sys.argv[2], index=index, gene_id=line_array[0], coor=line_array[1], strand=line_array[2], best_ara=line_array[3], gene_des =line_array[4])
        print(cmd)
        c.execute(cmd)
        index = index +1
        print(index)

conn.commit()
conn.close()



#dd = c.execute("SELECT * FROM %s" % sys.argv[2])
#print(dd)

