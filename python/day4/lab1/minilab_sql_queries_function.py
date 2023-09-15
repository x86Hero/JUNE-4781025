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


# How many sale did each employee make during Q2 of 2000
betweenQuery="SELECT emp_no, count(order_date) FROM sale WHERE order_date BETWEEN '2000-04-01' AND '2000-06-30' GROUP BY emp_no"
# Get me all the tel no. of Officers in our contacts list for a promo
likeQuery="SELECT contact_name,tel FROM contact WHERE job_title LIKE '%Officer%'"
# List all items that have a unit price under £10 - excluding * which indicates number of units sold
lessthanQuery="SELECT description FROM sale WHERE order_value < '10.00' AND description NOT LIKE '%*%'"
# get employees on less than or equal min living wage for surrey/london
inQuery="DECLARE @minLivingWage AS DECIMAL = 13.000 ; SELECT emp_no, first_name, salary FROM salesperson WHERE county in ('surrey','london') and salary <= @minLivingWage"
# get department name , manager and all employees from department '3'
equalQuery="SELECT dept.dept_no, dept.dept_name, dept.manager, salesperson.first_name, salesperson.last_name FROM dept INNER JOIN salesperson ON dept.dept_no = salesperson.dept_no WHERE dept.dept_no = 3"

print("Employees and their sales in Q2 2000: \n" + runQuery(betweenQuery) + "\n")
print("Officer contacts for marketing: \n" + runQuery(likeQuery) + "\n")
print("Units selling at or under 10 pounds: \n" + runQuery(lessthanQuery) + "\n")
print("Employees under or at min living wage: \n" + runQuery(inQuery) + "\n")
print("Manager and employee(s) working in Credit Control: \n" + runQuery(equalQuery) + "\n")