# calculate personal tax - with functions

#(1)
from logging.handlers import TimedRotatingFileHandler


def getIncomeTax(salary):
    allowance=11850

    if salary > allowance:
         taxableSalary=salary-allowance
    else:
         return "Your salary is below the threshold, you will not be taxed."

    if salary > 0 and salary <= 34500:
        incomeTax = taxableSalary * 0.2
        return incomeTax

    elif salary >= 34501 and salary <= 150000:
        incomeTax = taxableSalary * 0.4
        return incomeTax
    elif salary > 150000:
        incomeTax = taxableSalary * 0.45
        return incomeTax
    else:
        return "You did not enter a valid salary. Please enter an amount over 0."

userSalary = int(input("Please enter your salary to calculate your income tax: "))
taxed = getIncomeTax(userSalary)
print(taxed)



# ---------------------


# userSalary = totalamount 

# incomeTaxCalc function
#   allowance=11850
#   band1Threshold = 34500
#   band2Threshold = 150000
#   
#   if salary > allowance:
#         taxableSalary=salary-allowance
#   else:
#         return "Your salary is below the threshold, you will not be taxed."
#
#   if (salary - band1Threshold) 
#       
#   if salary > 0 and <= band1Threshold
#      incometax = taxableSalary * 0.2
#      
#   
#   if salary > band1Threshold and <= band2Threshold 
#      
#      remainder = salary - band1Threshold
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

