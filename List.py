# In List we use Square Brackets [ ].Main Difference is And in Tuple We use ( )Parenthesis.

# List Adding Elements are the append, insert, extend
num = [10, 15, 25]

# Append (item) – Add an item to the end of the list.
num.append(64)

# Insert (index, item) – Add an item at a specific index.
num.insert(0,23)

# Extend (iterable) – Add multiple items to the end of the list
num.extend([13,26])

# print(num)

# List Removing Elements are pop(), remove(), clear().
num1 = [25, 96, 74, 85, 59 ]

# pop(index) – Remove an item by index and return it
num1.pop(0)

# remove(value) – Remove the first occurrence of a value.
num1.remove(74)

# clear() – Remove all elements from the list
num1.clear()

print(num1)

# Intermediate Operations are the Slicing, list Length, Check Membership, Concatenation, 
# Repetition,Sorting, Copying a List

# slicing a list to access 

ab = [31, 32, 33, 34]

print(ab[0:3:2])

# Length() in a list
print(len(ab))

# Check Membership in List
print(31 in ab)    # Output: True
print(99 not in ab) # Output: True

# Concatenation in List
d = [10, 15,17]
f = [11,14, 16]
combined = d + f
print(combined)

# Repetition in list
repeated = [2] * 5
print(repeated)  

# Sorting in list
numbers = [5, 2, 9, 1]
numbers.sort()
print(numbers)  # Output: [1, 2, 5, 9]

# sorted() (creates a new sorted list)
sorted_numbers = sorted(numbers, reverse=True)
print(sorted_numbers)  # Output: [9, 5, 2, 1]

# Copying a List
new_list = numbers[:]
print(new_list)




