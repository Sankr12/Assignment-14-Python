# Write a python script to a element in a list with of their occurences

print()
num = int(input("Enter the number of elements you want to input: "))
num_list = []

for i in range(num):
    a = input()
    num_list.append(a)

print("\nOriginal List:")
print(num_list)

target_element = input("\nEnter the element you want to find the indices for: ")

indices = []
for index, items in enumerate(num_list):
    if items==target_element:
        indices.append(index)
    
if indices:
    print(f"\nIndices of occurrences of {target_element}:",end=' ')
    print(indices)
else:
    print(f"\n{target_element} is not found in the list.")
