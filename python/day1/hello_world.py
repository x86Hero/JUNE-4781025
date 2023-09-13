print("Hello World")

# data types
# Integer, any whole number - 5, -5, 0
# Floating, any fractional number - 1.1, 2.3, 000.00
# String, alphanumeric text - "cat", "hello world", "password1"
# Boolean, true or false - True / False 

mystring='my text' # string
myinteger=123 # integer
myfloat=123.45 # floating
myboolean=True # boolean

print(mystring)
print(myinteger)
print(myfloat)
print(myboolean)

# Variables should follow camel case. start lower case, then every other word starts with uppercase.
# ---- example ----
# myString="London"


# Input
input() # will pause program, so user can type something in.
# You can add string inside the input brackets to describe what the users should input.
# You can also assign the input to a variable
randomWords = input("Enter some words: ")
print(randomWords) # you can then return the users input by printing the variable


# Variable manipulation
textVar1="Hello"
textVar2="World"

print(textVar1 + " beautiful " + textVar2)

# integer operations
num1=12
num2=50
print(num1 + num2)


# casting - converting data from one type to another in memory.
# Get age and store as ine
age=int(input("Please enter your age: "))

# concat string and int by using ',' as separators
print("You are" , age , "years old")

# convert age (int) to string (str) and concat using '+'
print(str(age) + " Is a young age :)")

# print two lines, second print is doing a calculation using age (int)
print("Your age next year will be: ")
print(age + 1 )

# casting to float
coffeeCost=float(input("How much does a coffee cost?: "))
print(coffeeCost)

# converting to int from float, will drop the decimal places - IT WILL NOT DO ANY ROUNDING
print(int(coffeeCost))

# casting to boolean
textVar1="Hello"
print(bool(textVar1))
# anything that is not zero, boolean will return True

# anything that is 0, it will return False
# any string that is not empty "", boolean will return True
# any string that is empty "", boolean will return False


# you can find the type of a variables by using type()
type(textVar1)