# Python supports dynamic typing, we can assign any data type to it.
a = 5
print(type(a))

a = 0.2
print(type(a))

# String & Operations

a = "Hello World"
print(type(a))

a = "I can write this as I'm Python"
print(a)

# Get String's Length
print(len(a))

# String indexing 
# using forward indexing
print(a[0])
# using backward indexing
print(a[-1])

# String Slicing
# stop index is exclusive
print("Hello World"[8])
print(a[:5])
print(a[5:])
print(a[5:9])
# using step size in slicing
print(a[::]) # this will print the whole string
print(a[::2]) # jump in step size of 2
print(a[5:20:2]) # combination of start index, end index and step size
print(a[::-1]) # trick to reverse a string

# String Properties & Methods

# Strings are immutable
a = "Hello"
# a[0] = 'C' # not allowed, it will give error

# String concatenation
a = a + " World"
print(a)

# String Cases change
print(a.upper())
print(a.lower())

# Split a string
print(a.split(' '))

# String formatting methods
a = "string {} here and {} here".format("one", "two")
print(a)
a = "string {1} here and {0} here".format("two", "one") # provide indexes to get arguments from format method
print(a)
a = "string {i} here and {ii} here".format(i = "two", ii = "one") # variables to arguments from format method
print(a)

a = 10/3
print("Value {}".format(a))
# Adding width & precision
print("Value {r:1.3}".format(r=a))

# New implementation of format method from python 3.6
a = "Hello"
print(f'{a} World')

# Booleans: True & False are not equal to true & false
print(True)
print(False)
type(True)