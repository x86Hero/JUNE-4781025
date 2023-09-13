
# Part 1

#(1)
ages = [12,18,33,84,45,67,12,82,95,16,10,23,43,29,40,34,30,16,44,69,70,74,38,65,36,83,50,11,79,64,78,37,3,8,68,22,4,60,33,82,45,23,5,18,28,99,17,81,14,88,50,19,59,7,44,93,35,72,25,63,11,69,11,76,10,60,30,14,21,82,47,6,21,88,46,78,92,48,36,28,51]
agesLen=len(ages)
print("List length:",agesLen)

#(2)
for age in ages:
	print(age)

print("--------")

#(3)
for count in range(0,agesLen):
	print("index item",count,"is currently",ages[count])
	ages[count] += 1
	print("index item",count,"has been incremented to",ages[count])

print("--------")

#(4)
for age in ages:
	if age < 16 or age > 65:
		print("removing",age,"from the list.")
		ages.remove(age)

for age in ages:
	print(age)

print("--------")

#(5)
for count in range(0,len(ages)):
	if ages[count] >= 16 and ages[count] <= 25:
		print("This age is within the limit:",ages[count])

print("--------")

#(6)
ages.sort()
print(ages)

#(7)
ageRangeCount=0
for age in ages:
	if age >= 16 and age <= 25:
		ageRangeCount += 1

print("16 to 25:", ageRangeCount,"/",len(ages))


# Part 2
# Task 1

#(1)
userString=input("Enter a word: ")
vowelCount=0
for letter in userString:
	if letter in ("a","e","i","o","u"):
		vowelCount+=1

print("There are",vowelCount,"vowels in this word.")

# Task 2
time1=input("Enter a day-time string formate DD:HH:MM : ")
time2=input("Enter a day-time string formate DD:HH:MM : ")

