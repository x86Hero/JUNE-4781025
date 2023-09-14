
#try catch
try:
    print("a" + 2)
except:
    print("You cannot add string and integers... ")


# try catch and obtain the original exception
try:
    print("a" + 2)
except Exception as e:
    print("You cannot concatenate string and integar. See exception: ")
    print(e)