# Write a python script to calculate the sum of elements in a given list of numbers.

print()
num = int(input("Enter how many elements you want: "))
L = []

for i in range(num):
    a = int(input())
    L.append(a)

print()
print("List:",L)
print("Sum of elements:",sum(L))
print()