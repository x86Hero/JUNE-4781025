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
        print("Issue running INSERT. Please see below error: \n")
        result = e
        
    #commit data
    conn.commit()
    #close connection
    conn.close()
    return result



# ------------------- main --------------------

# INSERT INTO TABLE_NAME (COL1,COL2,COL3)
# VALUES (VAL1,VAL2,VAL3)

# UPDATE salesperson SET post_code = 'E10 5HP'
# WHERE emp_no = 70

# DELETE FROM salesperson WHERE emp_no = 70

# Get records from salesperson
getSalesTeam= "SELECT * FROM salesperson"

# sql insert statement
writeStmnt = """INSERT INTO salesperson (emp_no, first_name, last_name, dept_no, salary, sales_target, county, post_code, tel, notes)
VALUES ('70','Ash','Lee','2','13.000','9.000','London','E105HG','07382947591','Ash is awesome!')
"""

# update value(s) on an existing record, based on a filter
updateStmnt = """UPDATE salesperson SET post_code = 'E10 5HP'
WHERE emp_no = 70
"""

# delete a record based on a filter
deleteStmnt = "DELETE FROM salesperson WHERE emp_no = 70"

# get the table rows before insert, insert the data and then check the rows again after.
#print(runQuery(getSalesTeam))
#print(writeQuery(writeStmnt))
#print(writeQuery(updateStmnt))
print(writeQuery(deleteStmnt))
print(runQuery(getSalesTeam))