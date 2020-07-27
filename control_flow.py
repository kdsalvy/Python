# If conditions

if True:
    print("It's True")

# If else conditions
hungry = True
if hungry:
    print("I'm Hungry")
else:
    print("I'm not Hungry")

# Nested else ifs
location = "bank"

if location == "shop":
    print("I'm at the shop")
elif location == "bank":
    print("I'm at the bank")
else:
    print("I'm Lost")
    

# For Loop
my_list = [1,2,3,4,5,6,7,8,9]
for item in my_list:
    print(item)
    
for item in my_list:
    if item % 2 == 0:
        print(f'Even No: {item}')
    else:
        print(f'Odd No: {item}')
