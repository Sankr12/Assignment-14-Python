# Write a python script to create a list of first even natural numbers.

print()
num = int(input("Enter a number: "))
i=1
list = []

while i<=num:
    list.append(i*2)
    i+=1
print(list)
print()