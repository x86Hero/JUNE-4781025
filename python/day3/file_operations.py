# file operations

# open a file, shown as file object
fileObject = open("python/day3/story.txt")
print(type(fileObject))

# read
fileStrings = fileObject.read()
print(fileStrings)

# count
print(fileStrings.count("skull"))

# replace
updatedStory = fileStrings.replace("skull island","turtle bay")
print(updatedStory)

# seek - return to the start of a file to read from the beginning
fileObject.seek(0)

# reading lines into a list
listLines = fileObject.readlines()
print(listLines[0])

# close the file
fileObject.close()

# ------------ writing

# open file for writing.

writeFileObject = open("python/day3/story.txt","w") # opens and deletes the file content
writeFileObject.write(updatedStory) # writing new content to file
writeFileObject.close() # close file


# with, auto closes.

with open("python/day3/story.txt") as file:
    lines = file.readlines()

