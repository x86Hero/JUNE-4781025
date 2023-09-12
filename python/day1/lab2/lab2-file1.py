# Part 1

# get user age and convert to int, store in userAge
userAge=int(input("Please enter your age in digits: "))

# Single IFs
if userAge >= 18:
	print("You are in category A")

if userAge >= 16:
	print("You are in category B")

if userAge < 16:
	print("You are in category C")


# Elif
if userAge >= 18:
	print("You are in category A")
elif userAge >= 16:
	print("You are in category B")
else:
	print("You are in category C")
