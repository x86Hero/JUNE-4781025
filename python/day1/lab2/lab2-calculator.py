# part 2

# collect users numbers
num1=int(input("Enter first number: "))
num2=int(input("Enter second number: "))

# print choice options
print("")
print("1. Add  +")
print("2. Subtract  -")
print("3. Multiply  *")
print("4. Divide  /")
print("5. Square  s")
print("")

# get user choice
operationChoice=input("Please select the operation from the above menu: ")

# perform operation based on user input, using if and elif
if operationChoice == "1" or operationChoice == "+":
    print(num1 + num2)
elif operationChoice == "2" or operationChoice == "-":
    print(num1 - num2)
elif operationChoice == "3" or operationChoice == "*":
    print(num1 * num2)
elif operationChoice == "4" or operationChoice == "/":
    print(num1 * num2)
elif operationChoice == "5" or operationChoice == "s":
    print(num1 ** num2)
else:
    print("The input is not valid, please type the menu number of operation symbol.")