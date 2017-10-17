temp = float(input('what is the temperature in celsius?'))
isIce = temp <= 0.0
isWater = temp > 0.0 and temp <= 100
isVapor = temp > 100
if (isIce):
	print ('ice')
elif (isWater):
	print ('water')
elif (isVapor):
	print ('vapor')
else:
	print ('error: does not compute')
