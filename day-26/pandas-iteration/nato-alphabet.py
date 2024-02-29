import pandas

student_dict = {
    "student": ["angela", "james", "lily"],
    "score": [56, 76, 98]
}

# Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(f"{student_data_frame}\n\n")

# loop through a data frame (essentially the same as dict example above)
# for (key, value) in student_data_frame.items():
#     print(value)

# loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row.student)
