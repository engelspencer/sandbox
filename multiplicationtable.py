table = []

for num1 in range(1,2001):
	table.append([])
	for num2 in range(1,2001):
		table[num1-1].append(num1 * num2)
for num1 in range(0,2000):
	print (table[num1])
