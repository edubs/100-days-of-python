# syntax
# new_dict = {new_key: new_value for (key,value) in dict.items() if test}
import random

names = ['alex', 'beth', 'caroline', 'dave', 'eleanor', 'freddie']

students_scores = {student: random.randint(1, 100) for student in names}
print(students_scores)
passed_students = {student: score for (student, score) in students_scores.items() if score >= 60}
print(passed_students)

# sentence = input("input a sentence: ")
# letter_count = {word: len(word) for word in sentence.split()}
# print(letter_count)

temp_c = {'monday': 12, 'tuesday': 14, 'wednesday': 15, 'thursday': 14, 'friday': 21, 'saturday': 22, 'sunday': 24}

# list comprehension on a dictionary
temp_f = {day: (temp * 9 / 5) + 32 for (day, temp) in temp_c.items()}
print(temp_f)
