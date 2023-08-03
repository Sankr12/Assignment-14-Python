# Write a python script to create a list of first N odd natural numbers

print()
num = int(input("Enter a number: "))
list = []
i=1

while i<=num:
    list.append(2*i-1)
    i+=1
print(list)
print()