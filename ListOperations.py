# Python List Operations with User Input

# 1️⃣ Take input from user
user_input = input("Enter numbers separated by space: ")
numbers = [int(x) for x in user_input.split()]  # Convert input to list of integers

print("\nOriginal List:", numbers)
print("----------------------")

# 2️⃣ Accessing Elements
print("First element:", numbers[0])
print("Last element:", numbers[-1])
print("Slice of first three elements:", numbers[:3])
print("----------------------")

# 3️⃣ Adding Elements
num_to_add = int(input("Enter a number to append: "))
numbers.append(num_to_add)

num_to_insert = int(input("Enter a number to insert: "))
index_to_insert = int(input("Enter index to insert at: "))
numbers.insert(index_to_insert, num_to_insert)

more_numbers = input("Enter more numbers separated by space to extend the list: ")
numbers.extend([int(x) for x in more_numbers.split()])

print("List after adding elements:", numbers)
print("----------------------")

# 4️⃣ Removing Elements
num_to_remove = int(input("Enter a number to remove (first occurrence): "))
if num_to_remove in numbers:
    numbers.remove(num_to_remove)
else:
    print(f"{num_to_remove} not in list.")

numbers.pop()  # Remove last element
del_index = int(input("Enter index to delete element: "))
if 0 <= del_index < len(numbers):
    del numbers[del_index]

print("List after removing elements:", numbers)
print("----------------------")

# 5️⃣ Searching
search_num = int(input("Enter a number to search: "))
if search_num in numbers:
    print(f"{search_num} found at index {numbers.index(search_num)}")
else:
    print(f"{search_num} not found in the list.")
print("----------------------")

# 6️⃣ Looping through list
print("Looping through list:")
for num in numbers:
    print(num, end=" ")
print("\n----------------------")

# 7️⃣ List Comprehension
squares = [x**2 for x in numbers]
evens = [x for x in numbers if x % 2 == 0]
print("Squares:", squares)
print("Even numbers:", evens)
print("----------------------")

# 8️⃣ Sorting
numbers.sort()
print("Sorted ascending:", numbers)
numbers.sort(reverse=True)
print("Sorted descending:", numbers)
print("Sorted without changing original:", sorted(numbers))
print("----------------------")

# 9️⃣ Other Useful Operations
print("Length:", len(numbers))
print("Sum:", sum(numbers))
print("Min:", min(numbers))
print("Max:", max(numbers))
numbers_copy = numbers.copy()
print("Copied list:", numbers_copy)
print("----------------------")

# 1️⃣0️⃣ Clearing the list
numbers.clear()
print("List after clear():", numbers)
