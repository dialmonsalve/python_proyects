import requests

""" response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()

longitude = data["iss_position"]["longitude"]

print(data)
print(longitude) """

parameters = {
	"lat":6.244203,
	"lng":-75.581215,
	"formatted":0
}

response = requests.get(url="http://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()

data = response.json()

print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]

print(f"sunrise: {sunrise}\nsunset: {sunset}")