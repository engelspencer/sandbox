convertNumber = int(input('please enter a number to be converted: '))
factorial = 1
for n in range(convertNumber+1):
	if (n > 0):
		factorial = factorial * n
print (factorial)
