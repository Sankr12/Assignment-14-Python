# Write a python script to calculate the sum of elements in a given list of numbers.

print()
num = int(input("Enter how many elements you want: "))
i = 0
list = []
b=0

while i<num:
    a = int(input())
    list.append(a)
    b=b+a
    i+=1

print()
print("List:",list)
print("Sum of elements:",b)
print()

    