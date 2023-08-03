print()
num = int(input("Enter the number of elements you want to input: "))
num_list = []

for i in range(num):
    a = int(input())
    num_list.append(a)

print("\nOriginal List:")
print(num_list)

target_element = int(input("\nEnter the element you want to find the indices for: "))

indices = [index for index, element in enumerate(num_list) if element == target_element]

if indices:
    print(f"\nIndices of occurrences of {target_element}:")
    print(indices)
else:
    print(f"\n{target_element} is not found in the list.")
