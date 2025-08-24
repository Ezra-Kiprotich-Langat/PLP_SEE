# (1) A program that writes data into a file
file = open("newFile.txt", "w")
file.write("Hello World!")

# A program that reads data in a file
file = open("newFile.txt", "r")
data = file.read()
print(data)

# (2)A program that asks the user for filename and handle errors if doesn't exist..
try:
    with open("newFile.txt", "r") as file:
        data = file.read()
        print(data)
except FileNotFoundError:
    print("File not found. Please check the filename.")