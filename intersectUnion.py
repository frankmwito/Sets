# create two sets and find the intersection, union and difference between them

n1 = int(input("Enter the maximum number of the first list:"))
set1 = set()

for i in range(n1):
    num1 = int(input("Enter the numbers of the first set:"))
    set1.add(num1)
print(f"your first set is: {set1}")

n2 = int(input("Enter the maximum number of the second list:"))
set2 = set()

for i in range(n2):
    num2 = int(input("Enter the numbers of the second set:"))
    set2.add(num2)
print(f"your second set is: {set2}")

set_union = set1.union(set2)
print(f"the union of the two sets is: {set_union}")

set_difference = set1.difference(set2)
print(f"the difference of the two sets is: {set_difference}")    

set_intersection = set1.intersection(set2)
print(f"the intersection of the two sets is: {set_intersection}")