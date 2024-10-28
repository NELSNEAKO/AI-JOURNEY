# 'is' is called identity operator

x = [1, 2, 3]
y = x       # y points to the same object as x
z = [1, 2, 3]  # z is a separate object with the same value as x and y

print(x is y)  # True, x and y are the same object in memory
print(x is z)  # False, x and z are different objects, even though they have the same content
print(x == z)  # True, x and z have the same values, so they are equal



# 'in' called membership operator

fruits = ["apple", "banana", "cherry"]

print("apple" in fruits)  # True, "apple" is a member of the list
print("orange" in fruits)  # False, "orange" is not in the list
