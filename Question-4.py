# Write a python script to find the greatest number in a given list of numbers

print()
num = int(input("Enter the elements you want to input: ")) 
list = []
i=0

while i<num:
    b = input()
    list.append(int(b))
    i+=1

print()
print("list:",list)
print()
print("Greatest number of list:",max(list))
print()