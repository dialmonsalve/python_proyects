import pandas

data = pandas.read_csv("08_pandas/weather_data.csv")

""" data_to_dict = data.to_dict()
print(data_to_dict) """

temp_list = data["temp"].to_list()
print(temp_list)

""" avr = 0
for temp in temp_list:
	avr += temp

print(avr/len(temp_list)) """

average = data.temp.mean()

print(average)

#Get data in row
row = data[data.day == "Saturday"]
print(row)

max_temp = data[data.temp == data.temp.max()]
print(max_temp)
