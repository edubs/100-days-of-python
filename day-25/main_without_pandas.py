# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()[1:]
#
# print(data)

import csv

with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    temperatures = []
    for row in data:
        # get column 1 (temperatures) into new list
        temperatures.append(row[1])

temperatures = [int(n) for n in temperatures[1:]]
print(temperatures)
