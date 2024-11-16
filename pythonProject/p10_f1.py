import sqlite3

connection = sqlite3.connect("itstep_DB.sl3", 5)
cur = connection.cursor()
cur.execute("CREATE rowid name FROM first_table;")
connection.commit()
res = cur.fetchall()
print(res)
connection.close()