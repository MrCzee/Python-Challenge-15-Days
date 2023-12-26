#1. Opening a File:

file = open("temp.txt", "r")
#file = open("new_file.txt", "w")  # [4]
# Open a file in append mode (adds content to the end)
#file = open("log.txt", "a")  # [4]

#2. Reading from a File:

#contents = file.read()
#print(contents)

# Read a single line
#line = file.readline()  # [6]

# Read all lines into a list
#lines = file.readlines()
file = open("temp.txt", "w")

# Write a string to the file
file.write("this is a tesing write string")

file = open("temp.txt", "r")
content = file.read()
print(content)

# Write multiple lines using a loop
#for line in lines:
 #   file.write(line)

#Closing a File
