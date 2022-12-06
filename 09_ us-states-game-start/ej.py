def add(*args:list):
	sum = 0
	for n in args:		
		sum += n
	return sum


add_nuum = add(5,3,5,8,4,9,7,10)

print(add_nuum)