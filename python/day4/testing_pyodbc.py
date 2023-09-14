#import modules
import pyodbc
#create sql server connection string
connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
#create connection object with the string
conn = pyodbc.connect(connectionString)
#create a db cursor to execute commands
cur = conn.cursor()




# queries

# basic example: SELECT <COLUMN NAME> FROM <TABLE NAME>

# get table names
for table in cur.tables(schema="dbo"):
    print(table.table_name)

# get all rows from company
for row in cur.execute('SELECT * FROM company').fetchall():
    print(row)

# get all column names from table
for column in cur.columns(table="company").fetchall():
    print(column)

# storing query in variable
selectAllSale = "SELECT * FROM sale"
for row in cur.execute(selectAllSale).fetchall():
    print(row)




#close connection
conn.close()
#loop through results

