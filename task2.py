import pandas as pd
import sqlite3
conn=sqlite3.connect("db1.db")
cursorObject=conn.cursor()
cursorObject.execute("CREATE TABLE imgfg(id string, img blob)")
conn.commit()

im=open('/Users/natalieqoursha/Documents/images//img1.png','rb').read()

conn.commit()
table = pd.read_sql_query("SELECT * FROM imgfg", conn)
table.to_csv("imgfg" + '.csv', index_label='index')
print(table)