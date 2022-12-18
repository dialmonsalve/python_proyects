def logging_decorator(func):
	def wrapper(*args, **kwargs):

		print(f"you call a function {func.__name__}{args}")

		result = func(args[0], args[1], args[2])
		print(f"It returned: {result}")

	return wrapper

@logging_decorator
def total(a, b, c):
	return a * b * c

total(5,5,5)

