my_file = open('input.txt')
print(my_file.read())
# The curson has moved to end so nothing will print
print(my_file.read())
# Reset the cursor
my_file.seek(0)
print(my_file.read())

# Get each line in a list
my_file.seek(0)
print(my_file.readlines())

# Close the file 
my_file.close()

#Auto close a file
with open("input.txt") as my_new_file:
    contents = my_new_file.read()
    print(contents)
    

# Read a file by using mode (default permissions)
# mode = r(read), w(overwrite old file or create new), a(append to existing file), r+(reading and writing), w+(writing and reading: Overwrites exiting file or create new)

with open('input.txt', mode='r') as my_new_file:
    contents = my_new_file.read()
    print(contents)

#Mode = a
with open('input.txt', mode='a') as my_new_file:
    my_new_file.write("Line Six")
    
with open('input.txt', mode='r') as my_new_file:
    contents = my_new_file.read()
    print(contents)

# Mode = w
with open('input-write.txt', mode='w') as my_new_file:
    my_new_file.write("Hello World")