filename = input("Filename: ")

with open(filename) as file:
	data = file.read().split("\n")

for number_1 in data:
	n1 = int(number_1)
	for number_2 in data:
		n2 = int(number_2)
		for number_3 in data:
			n3 = int(number_3)
			if number_1 != number_2 and number_2 != number_3:
				if n1 + n2 + n3 == 2020:
					print(f"{n1} * {n2} * {n3} = {n1 * n2 * n3}")