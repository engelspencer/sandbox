snum = input('Is your number strong? ')
sum = 0
for sdigit in snum:
	digit = int(sdigit)
	factorial = 1
	for x in range(1,digit+1):
		factorial = factorial * x
	print (sdigit + '! = ' + str(factorial))
	sum = sum + factorial
if (int(snum) == sum):
	print ('The number is strong!')
else:
	print ('The number is not strong.')
