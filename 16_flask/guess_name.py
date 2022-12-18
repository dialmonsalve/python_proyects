from flask import Flask, render_template
import requests


app = Flask(__name__)

@app.route('/')
def home():
	return "Home"

@app.route("/<name>")
def guess_name(name):

	response_age = requests.get(url=f"https://api.agify.io?name={name}")
	response_gender = requests.get(url=f"https://api.genderize.io/?name={name}")

	age = response_age.json()
	gender = response_gender.json()

	return render_template("guess_name.html",name=name, age=age["age"], gender=gender["gender"])

if __name__ == ("__main__"):
	app.run(debug=True)
