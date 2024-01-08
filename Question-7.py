# Write a python script to remove all non int values from a list

print()
num = int(input("Enter the elements you want to input: "))
li = []

for i in range(0,num):
    a=input()
    li.append(a)

updated_list = []

for item in li:
    if item.isdigit():
        updated_list.append(item)

print()
print(updated_list)
print()