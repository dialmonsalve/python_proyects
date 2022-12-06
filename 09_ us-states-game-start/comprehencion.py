numbers = [1, 2, 3]

new_list = []



for n in numbers:
	add_1 = n + 1

	new_list.append(add_1)

print(new_list)


print(f"{'-' * 15}the same path{'-' * 15}")
new_list_2 = [ n + 1 for n in numbers]

print(new_list_2)