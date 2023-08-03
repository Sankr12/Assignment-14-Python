# Write a python script to remove all non int values from a list

print()
num = int(input("Enter the elements you want to input: "))
i = 0
list = []

while i<num:
    try:
        a=int(input())
        list.append(a)
    except ValueError:
        pass
    i+=1
print()
print(list)
print()
