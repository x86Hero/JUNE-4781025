# open  file

companies = []
sales = []
grandTotal = 0
monthTotal = 0

with open("python/day3/lab3/carSale.csv") as file:
    lines = file.readlines()

for line in lines:
    print(line)
    data = line.strip().split(',')
    companies.append(data[0])
    sales.append(list(map(int,data[1:])))

for listitem in sales:
    grandTotal += sum(listitem)

# need to work out how to add up all the values for each month
for x in range(0,len(sales)):
    for item in sales[x]:
        monthTotal += item[x]
    print(monthTotal)
    
print("The total number of sales from data: ", grandTotal)
        
