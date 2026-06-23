'''Create a Python script that opens a file called lyrics.txt and prints the file pointer's current position using tell() before and after reading the first 10 characters.'''
# Open file in read mode
# Step 1: Write to file (create/overwrite)
file = open("lyrics.txt", "w")
file.write("Hello this is a sample lyrics file")
file.close()


# Step 2: Now read the file
file = open("lyrics.txt", "r")

print("Position before reading:", file.tell())

data = file.read(10)

print("Position after reading:", file.tell())

file.close()