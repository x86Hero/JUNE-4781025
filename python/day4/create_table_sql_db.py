#import modules
import pyodbc

def getQueryData(sqlQuery):
    #create sql server connection string
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    #create connection object with the string
    conn = pyodbc.connect(connectionString)
    #create a db cursor to execute commands
    cur = conn.cursor()
    result = cur.execute(sqlQuery).fetchall()
    #close connection
    conn.close()
    return result

def runQuery(qString):
    data = getQueryData(qString)
    rowList = (list(map(str,data)))
    rows='\n'.join(rowList[0:])
    return rows

def writeQuery(statement):
    #create sql server connection string
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    #create connection object with the string
    conn = pyodbc.connect(connectionString)
    #create a db cursor to execute commands
    cur = conn.cursor()

    # try catch code.
    try:
        result = cur.execute(statement)
    except Exception as e:
        print("Write statement failed. Please see below error: \n")
        result = e
        
    #commit data
    conn.commit()
    #close connection
    conn.close()
    return result

gameTable = "CREATE TABLE Games ( ID int NOT NULL, game_title nvarchar(40) NOT NULL, game_age_rating nvarchar(2) NOT NULL, console nvarchar(40) NOT NULL, stock int NULL )"
dropTable = "DROP TABLE Games"
writeQuery(dropTable)