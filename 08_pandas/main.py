import pandas

data = pandas.read_csv("08_pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

sum_gray = data[data["Primary Fur Color"] == "Gray"]
sum_cinnamon = data[data["Primary Fur Color"] == "Cinnamon"]
sum_black = data[data["Primary Fur Color"] == "Black"]

data_dict = {
	"Fur Color": ["Gray", "Cinnamon", "Black"],
	"Count" :[len(sum_gray), len(sum_cinnamon), len(sum_black)]
}

data_frame = pandas.DataFrame(data_dict)

data_frame.to_csv("08_pandas/data.csv")

