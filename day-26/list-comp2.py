with open("file1.txt") as file1:
    list1 = file1.readlines()
with open("file2.txt") as file2:
    list2 = file2.readlines()

result = [int(y) for y in list1 if y in list2]
# Write your code above 👆
print(result)
