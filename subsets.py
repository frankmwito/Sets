# function that takes two sets and returns 'true' if one set is a subset of another

def check_subset(set1, set2):
    # Check if set1 is a subset of set2 or set2 is a subset of set1
    if set1.issubset(set2) or set2.issubset(set1):
        return True
    else:
        return False

# Input and creation of the first set
n1 = int(input("Enter the number of elements for the first set: "))
set1 = set()

for i in range(n1):
    num1 = int(input(f"Enter element {i+1} for the first set: "))
    set1.add(num1)

print(f"Your first set is: {set1}")

# Input and creation of the second set
n2 = int(input("Enter the number of elements for the second set: "))
set2 = set()

for i in range(n2):
    num2 = int(input(f"Enter element {i+1} for the second set: "))
    set2.add(num2)

print(f"Your second set is: {set2}")

# Check if one set is a subset of the other
result = check_subset(set1, set2)
print(f"Is one set a subset of the other? {result}")
