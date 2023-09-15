# importing and using pyodbc connect.

#import modules
import pyodbc
#create sql server connection string
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
#create connection object with the string
conn = pyodbc.connect(connectionString)
#create a db cursor to execute commands
cur = conn.cursor()
#run a query using cursor execute and store in results
result = cur.execute('SELECT * FROM company').fetchall()
#close connection
conn.close()
#loop through results
for row in result:
    print(row)



