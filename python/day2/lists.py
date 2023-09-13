# lists
["cake","biscuits","cannedfish","sparklingwater","carrots","potatoes"]
[1,3,5,7]

# printing
print(["my","list"])

# store to a variable
shoppingList = ["cake","biscuits","cannedfish","sparklingwater","carrots","potatoes"]
oddNums = [1,3,5,7]
boolList = [True,False,True]
print(shoppingList)
print(oddNums)

# looping
for item in shoppingList:
    print(item)

# get item by index
print(shoppingList[0]) # get items from start of list.
print(shoppingList[-1]) # get items from back of list.
print(shoppingList[2:4]) # get items with a range ':', not including the last number only the numbers from 2 up to 3
print(shoppingList,oddNums,boolList) # printing multiple lists

# nested list
megalist = [shoppingList,oddNums,boolList] # creating a list of lists :)
print(megalist)
print(megalist[0][0]) # query the lists within a list , this would search for first list 'shopping List' then return the first item from it.

# list length
print(len(megalist))

# Strings are lists
string="Ashley Lee"

for letter in string:
    print(letter)

print(string[4]) # you can also show a letter based on index.
print(string[0:7])

# appending to the end of list
print(shoppingList)
shoppingList.append("catfood")
print(shoppingList)