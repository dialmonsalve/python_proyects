from flask import Flask

app = Flask(__name__)

def make_bold(func):
	def wrap():
		return (f"<b>{func()}</b>")
	return wrap

def make_emphasis(func):
	def wrap():
		func()
		return (f"<em>{func()}</em>")
	return wrap

def make_underliner(func):
	def wrap():
		return (f"<u>{func()}</u>")
	return wrap

@app.route('/')
def hello_world():
	return 'Hello world'

@app.route('/bye')
@make_bold
@make_emphasis
@make_underliner
def bye():
	return f"Hello"


if __name__ =="__main__":
	app.run(debug=True)