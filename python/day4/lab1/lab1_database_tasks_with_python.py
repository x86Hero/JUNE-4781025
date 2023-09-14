import pyodbc

def sqlConn():
    #create sql server connection string
    connectionString = r'DRIVER={ODBC Driver 13 for SQL Server};SERVER=.\SQLExpress;DATABASE=qastore;Trusted_Connection=yes'
    #create connection object with the string
    conn = pyodbc.connect(connectionString)
    return conn

def sqlCur(connection):
    #create a db cursor to execute commands
    cur = connection.cursor()
    return cur

def createTable(statement):
    conn = sqlConn()
    cur = sqlCur(conn)

    # try catch code.
    try:
        result = cur.execute(statement)
    except Exception as e:
        print("Creating table failed. Please see below error: \n")
        result = e
        
    #commit data
    conn.commit()
    #close connection
    conn.close()
    return result

def getTableColumns(tableName):
    conn = sqlConn()
    cur = sqlCur(conn)

    #run a query using cursor execute and store in results
    result = cur.execute('SELECT * FROM {}'.format(tableName)).fetchall()
    columns = [result[0] for result in cur.description]
    return columns

def bulkdInsertTable(data, table):
    conn = sqlConn()
    cur = sqlCur(conn)
    insertStatements = []
    columnNames = []
    try:
        columnNames = getTableColumns(table)
    except Exception as e:
        print("Failed to obtain column info from the table name provided. Please see error: \n")
        result = e

    # try catch code.
    try:
        for row in data:
            insertStatements.append("INSERT INTO {} ".format(table) +  "({},{},{},{},{})".format(*columnNames[0:]) + " VALUES ('{}','{}','{}','{}','{}')".format(*row[0:]))
            
    except Exception as e:
        print("Failed to create bulk statements with data provided. Please see below error: \n")
        result = e

    #print(insertStatements)

    try:
        for statement in insertStatements:
            result = cur.execute(statement)
    except Exception as e:
        print("Failed to create bulk statements with data provided. Please see below error: \n")
        result = e
        
    #commit data
    conn.commit()
    #close connection
    conn.close()
    return result


def insertTable(statement):
    conn = sqlConn()
    cur = sqlCur(conn)

    # try catch code.
    try:
        result = cur.execute(statement)
    except Exception as e:
        print("Failed to insert into table. Please see below error: \n")
        result = e
        
    #commit data
    conn.commit()
    #close connection
    conn.close()
    return result



# ----------- main

# (1) Create student table
studentTable = """ 
CREATE TABLE Student ( 
    StudentID int NOT NULL, 
    FirstName nvarchar(40) NOT NULL, 
    Surname nvarchar(30) NULL, 
    Course nvarchar(30) NULL, 
    City nvarchar(15) NULL 
)
"""
createTable(studentTable)


#(2) Insert data into table
studentData = [["1","Ashley","Lee","Maths","London"],
               ["2","Charlie","Stones","Science","Manchester"],
               ["3","Dale","Jones","Maths","Manchester"],
               ["4","Danielle","James","IT","Bristol"],
               ["5","Finn","Adams","IT","London"],
               ["6","Scott","Taylor","Science","Brighton"]
              ]
#print(studentData)
print(bulkdInsertTable(studentData,"Student"))