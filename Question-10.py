# Write a python script to sort a list.

print()
num = int(input("Enter the number of elements you want to input: "))
num_list = []

for i in range(num):
    a = int(input())
    num_list.append(a)

print("\nOriginal List:")
print(num_list)

sorted_list = sorted(num_list)

print("\nSorted List:")
print(sorted_list)
