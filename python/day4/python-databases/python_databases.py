# importing and using pyodbc connect.

import pyodbc # import module to connect

connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes' # connection string

conn = pyodbc.connect(connectionString) # store connection string as an object

cur = conn.cursor() # this manages the commands we want to send

result = cur.execute('SELECT * FROM company').fetchall() # using cur object to execute comamnds.

conn.close() # close db connections

for row in result: # loop through each row and return everything.
    print(row)