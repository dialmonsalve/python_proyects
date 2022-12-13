import os
import requests
from datetime import datetime

API_ID = os.getenv("NUTRITION_APP_ID")
API_KEY = os.getenv("NUTRITION_API_KEY")

USERNAME = os.getenv("SHEETY_USER")
PASSWORD =os.getenv("SHEETY_PASSWORD")
NAME_VALIDATION=os.getenv("SHEETY_VALIDATION")
PROJECT_NAME =os.getenv("SHEETY_PROJECT")
SHEET = os.getenv("SHEETY_SHEET_NAME")

natural_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
shetty_endpoint = f"https://api.sheety.co/{NAME_VALIDATION}/{PROJECT_NAME}/{SHEET}"

parameters = {
	"query":"ran 10 miles",
	"gender":"female",
	"weight_kg":72.5,
	"height_cm":167.64,
	"age":30
}

headers = {
    "x-app-id": API_ID,
    "x-app-key": API_KEY,
}

response = requests.post(url=natural_endpoint, json=parameters, headers=headers)

result = response.json()

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        SHEET: {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
		
    }

    sheet_response = requests.post(
		url= shetty_endpoint, 
		json=sheet_inputs,
		auth=(
			USERNAME, 
			PASSWORD,
		)
	)
print(sheet_response.text)




