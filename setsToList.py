# create a set from a list and remove any duplicates

n1 = int(input("Enter the maximum number of elements:"))
numbers = []

for i in range(n1):
    num = int(input(f"Enter the elements of your choice {i+1}:"))
    numbers.append(num)

my_set = set(numbers)
print(f"this is the new set without the duplicates: {my_set}")