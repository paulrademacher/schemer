import pprint

import psycopg2

conn = psycopg2.connect("dbname=schemer")

curs = conn.cursor()

#curs.execute("Select * FROM oids;")
#pprint.pprint(curs.description)

#curs.execute("""SELECT * FROM information_schema.tables
#       WHERE table_schema = 'public'""")
curs.execute("""SELECT * FROM information_schema.columns""")
for table in curs.fetchall():
    print(table)
