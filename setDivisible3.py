# given a list of numbers, write a python program to find the set of numbers that are divisible by 3

n1 = int(input("Enter the size of your list:"))
numbers = list()

for i in range(n1):
    numbers.append(int(input(f"Enter a number {i+1}:")))

my_set = set(numbers)
numbers2 = set()

for number in my_set:
    if number % 3 == 0:
       numbers2.add(number)
    else:
        print("Not divisible by 3")
        
print(f"Numbers divisible by 3: {numbers2}")
    