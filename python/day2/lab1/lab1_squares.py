# Squares
num = 1

while num <= 100: #(2)
	print(num, "squared =", num * num) #(3)
	if (num * num) > 2000: #(4)
		print("Squared numbers has exceeded 2000")
		break
	num += 1