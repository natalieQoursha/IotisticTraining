Last login: Wed Jul  6 22:20:40 on ttys000
(base) natalieqoursha@natalies-Air ~ % python3
Python 3.9.12 (main, Apr  5 2022, 01:53:17) 
[Clang 12.0.0 ] :: Anaconda, Inc. on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>> import pandas as pd
>>> import sqlite3
>>> conn=sqlite3.connect("db1.db")
>>> cursorObject=conn.cursor()
>>> conn.commit()
>>> print(table)
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'table' is not defined
>>> import pandas as pd
>>> import sqlite3
>>> conn=sqlite3.connect("db1.db")
>>> cursorObject=conn.cursor()
>>> cursorObject.execute("CREATE TABLE imgfg(id string, img blob)")
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
sqlite3.OperationalError: table imgfg already exists
>>> conn.commit()
>>> 
>>> im=open('/Users/natalieqoursha/Documents/images//img1.png','rb').read()
>>> 
>>> conn.commit()
>>> table = pd.read_sql_query("SELECT * FROM imgfg", conn)
>>> table.to_csv("imgfg" + '.csv', index_label='index')
>>> print(table)
        id                                                img
0  pattern  b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\...
>>> 
