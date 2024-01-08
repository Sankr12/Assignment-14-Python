# Write a python script to sort a list.

print()
num = int(input("Enter the number of elements you want to input: "))
num_list = []

for i in range(num):
    a = int(input())
    num_list.append(a)

print("\nOriginal List:")
print(num_list)

for i in range(len(num_list)):
    for j in range(0, len(num_list)-i-1):
        if num_list[j]>num_list[j+1]:
            num_list[j], num_list[j+1] = num_list[j+1], num_list[j]

print(num_list)