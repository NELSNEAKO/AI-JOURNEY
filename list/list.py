fruits = ["apple", "banana", "cherry"]

#accesing
print(fruits[0])  # Output: apple
print(fruits[1])  # Output: banana

#modifying list
fruits[1] = "blueberry"  # Change "banana" to "blueberry"
print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

fruits.append("orange")  # Add "orange" to the end
print(fruits)  # Output: ['apple', 'blueberry', 'cherry', 'orange']

fruits.remove("apple")   # Remove "apple"
print(fruits)  # Output: ['blueberry', 'cherry', 'orange']

#using lists in loops
for fruit in fruits:
    print(fruit)
    