# 3 casting variables - calculate area and perimeter of the rectangle

# get user input and cast to int, store in length variable
length = int(input("Please enter the length of the rectangle: "))
# get user input and cast to int, store in width variable
width = int(input("Please enter the height of the rectangle: "))

# print the area calculation using length and width (l*w)
print("The area of this rectangle is", length * width)
# print the perimeter calculation using length and width (2*(l+w))
print("The perimeter of this rectangle is", 2*(length + width))
