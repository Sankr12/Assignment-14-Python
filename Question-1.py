# Write a python script to create a list of first N natural numbers

print()
num = int(input("Enter a number: "))
i = 1
list = []

while i<=num:
    list.append(i)
    i+=1

print(list)
print()