# Tuples are immutable
t = (1, 2, 3, 1, 2, 3, 1)
t_mix = (1,"Hello World", 1.2)

print(t)
print(t_mix)

#indexing
print(t[0])

#count occurences
print(t.count(1))

#get index of
print(t.index(2))