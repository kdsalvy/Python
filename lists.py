# List

#same data type list
my_list = [1,2,3,4]
print(my_list)

#multi data type list
my_list = ['Hello World', 1234, 12.34, 4, 5, 6, 7]
print(my_list)

#list length
print(len(my_list))

#list indexing : Works same as string
print(my_list[0])

#list slicing
print(my_list[:5])
print(my_list[5:])
print(my_list[2:5])
print(my_list[::-1])
print(my_list[2:6:2])

# list concatenation
my_list = my_list + [9, 8, 7, 11]
print(my_list)

# lists are mutable so the elements can be changed
my_list[0] = "My World"
print(my_list)

# add elements to the end of the list
my_list.append("Python")
print(my_list)
# remove element from the end of the list
print(my_list.pop())
# remove from an index
print(my_list.pop(2))

my_list = ['v','d','r','w','c','a']
# Sort the list
my_list.sort()
print(my_list)