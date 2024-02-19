numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [n * n for n in numbers]
print(squared_numbers)

list_of_strings = input("input list of nums: ").split(' ')
converted = [int(n) for n in list_of_strings]
result = [i for i in converted if i % 2 == 0]
print(result)
