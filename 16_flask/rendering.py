from flask import Flask, render_template
import datetime



app = Flask(__name__)

@app.route('/')
def home():
	current_year = datetime.datetime.now().year

	params = {
		"year":current_year
	}

	name = "Diego Alejandro Monsalve Estrada"
	return render_template('index.html', my_name=name, year=params)


if __name__ == '__main__':
	app.run(debug=True)
