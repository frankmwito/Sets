# remove all elements from a set that are also present in a list

# Input for the list
n1 = int(input("Enter the size of your list: "))
numbers = []

for i in range(n1):
    numbers.append(int(input(f"Enter number {i+1}: ")))

print(f"Your list is: {numbers}")

# Input for the set
n2 = int(input("Enter the size of your set: "))
numbers1 = set()

for i in range(n2):
    numbers1.add(int(input(f"Enter number {i+1}: ")))

print(f"Your set is: {numbers1}")

# Remove all elements from the set that are also present in the list
numbers1.difference_update(numbers)

print(f"Here is the set with all the removed elements: {numbers1}")
