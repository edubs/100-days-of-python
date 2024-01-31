import pandas

# data = pandas.read_csv("weather_data.csv")
#
# data_dict = data.to_dict()
# data_list = data["temp"].to_list()

# # old way with list math
# print(sum(data_list) / len(data_list))
#
# # data series function
# print(data["temp"].mean())
#
# # max function
# print(data["temp"].max())
#
# # get data in columns
# print(data["condition"])
# print(data.condition)

# get data in row
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print((monday.temp[0] * 9 / 5) + 32)

# create a dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# print(data)

# squirrel data exercise
data = pandas.read_csv('squirrel_data.csv')

count_gray_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
count_red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
count_black_squirrels = len(data[data["Primary Fur Color"] == "Black"])
print(count_gray_squirrels)
print(count_red_squirrels)
print(count_black_squirrels)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [count_gray_squirrels, count_red_squirrels, count_black_squirrels]
}

print(data_dict)
df = pandas.DataFrame(data_dict)
df.to_csv('squirrel_count.csv')
