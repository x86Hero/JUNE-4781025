# stats with functions

#(1,2,3)
data="100,30,53,67,85,87,50,45,51,72,64,69,59,17,22,23,44,25,16,67,85,87,50,45,51,72,59,14,50,55,32,23,24,25,37,28,39,30,33,35,40,34,41,43,94,95,59,98,99,44,45,47,48,49,53,61,63,69,75,77,60,83" 

#(4)
grades = data.split(',')
print(type(grades))
print(grades)

#(5)
print(min(grades))

#(6)
print(max(grades))

#(7,8)
# values are 100 and 99.
# this is because the list items are string 
print(type(grades[0]))

#(9) using list to cast 'grades' back into itself, but using map to convert the items to int
grades = list(map(int, grades))

#(10)
print(min(grades))
print(max(grades))