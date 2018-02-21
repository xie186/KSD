import sqlite3
con = sqlite3.connect('db.sqlite3')
cursor = con.cursor()
cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
print(cursor.fetchall())

tab_col = cursor.execute("PRAGMA table_info({tab_name})".format(tab_name="genewiki_app_gene"))
print(cursor.fetchall())
#for line in tab_col:
#    print(tab_col)
