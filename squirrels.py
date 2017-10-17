sunny = input('Is it sunny? (y/n) ')
hour = int(input('What is the hour of the day? '))

isSunnyOutside = sunny == 'y'
isBetween4and8 = hour >= 4 and hour <= 8

if (isSunnyOutside and isBetween4and8):
	print ('The squirrels are playing outside.')
else:
	print ('The squirrels are sleeping.')
