# calculate personal tax - with functions

#(1)
def getIncomeTax(salary):
    allowance=12570
    taxBand1Limit=50270
    taxBand2Limit=125140

    if salary > taxBand2Limit:
        incomeTax = ((salary - taxBand2Limit) * 0.45) + (((taxBand2Limit - taxBand1Limit) + allowance) * 0.4) + ((taxBand1Limit - allowance) * 0.2)
        return incomeTax
    elif salary > taxBand1Limit and salary < taxBand2Limit:
        incomeTax = ((salary - taxBand1Limit) * 0.4) + ((taxBand1Limit - allowance) * 0.2)
        return incomeTax
    elif salary > allowance and salary <= taxBand1Limit:
        incomeTax = (salary - allowance) * 0.2
        return incomeTax
    else:
        return "Your salary is below the threshold, you will not be taxed."
        
result = getIncomeTax(52000)
print(result)