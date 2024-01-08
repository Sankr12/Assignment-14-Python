# # Write a python script to print distinct elements along with their frequencies of occurence in the list

# print()
# num = int(input("Enter the number of elements you want to input: "))
# num_list = []

# for i in range(num):
#     a = int(input())
#     num_list.append(a)

# print("\nOriginal List:")
# print(num_list)

# frequency_dict = {}

# for element in num_list:
#     if element in frequency_dict:
#         frequency_dict[element] += 1
#     else:
#         frequency_dict[element] = 1

# print("\nDistinct Elements with their Frequencies:")
# for element, frequency in frequency_dict.items():
#     print(f"{element}: {frequency}")


from collections import Counter

print()
num = int(input("Enter the number of elements you want to input: "))
num_list = []

for i in range(num):
    a = input()
    num_list.append(a)

print("\nOriginal List:")
print(num_list)

counter = Counter(num_list)

print("\nDistinct Elements with their Frequencies:")
for element, frequency in counter.items():
    print(f"{element}: {frequency}")