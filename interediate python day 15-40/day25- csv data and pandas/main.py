import pandas as pd

# import csv
# with open("weather-data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1]!="temp":
#             temperatures.append((int(row[1])))
#     print(temperatures)

# data = pd.read_csv("weather-data.csv")
# temp_series = data["temp"]
# print(temp_series.mean())
# print(temp_series.max())
# print(data[data.temp == data.temp.max()])
#
# sunday = data[data.day == "Sunday"]
# print(sunday.condition)
# sun_temperature = sunday.temp
# print((sun_temperature*1.8)+32)


# Squirrel data
data = pd.read_csv("Squirrel_Data.csv")

cinnamon_sq = data[data["Primary Fur Color"] == "Cinnamon"]
gray_sq = data[data["Primary Fur Color"] == "Gray"]
Black_sq = data[data["Primary Fur Color"] == "Black"]

squirrels_data = {
    "Fur Color": ["Gray", "Red","Black"],
    "Count":[len(cinnamon_sq),len(gray_sq),len(Black_sq)]
}

df = pd.DataFrame.from_dict(squirrels_data)
df.to_csv("squirrels_count.csv")
# print(cinnamon)