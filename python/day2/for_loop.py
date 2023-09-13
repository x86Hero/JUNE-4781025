# for loop

# basic form

# loop using range.
for num in range(4):
    print(num)
print(" ")
# loop with a starting point in range.
for num in range(2,8):
    print(num)
print(" ")
# loop with a starting point in range, going backwards.
for num in range(8,2,-1):
    print(num)
print(" ")
# loop with a starting point in range, incrementing by 5
for num in range(5,100,5):
    print(num)

# NOTE: The last number in the range is not output, because num will reach the end of the range
#       and then the condition is met. 
