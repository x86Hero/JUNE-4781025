#import modules
import pyodbc
#create sql server connection string
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
#create connection object with the string
conn = pyodbc.connect(connectionString)
#create a db cursor to execute commands
cur = conn.cursor()


# queries
for row in cur.tables(catalog="QAStore",schema="dbo"):
    print(row.table_name)


#close connection
conn.close()
#loop through results

