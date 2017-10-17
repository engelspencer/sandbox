import random

number = random.randint(1,20)
guess = 0
iteration = 0

print ("My number is between 1 and 20")

while (guess != number and iteration < 5):
	guess = int(input("Guess my number: "))
	if (guess == number):
		print("You got it!")
	elif (guess != number):
		if (guess < number):
			print("Your guess is too low.")
		else:
			print("Your guess is too high.")
		print("Try again")
	iteration=iteration+1
	if (iteration == 5 and guess != number):
		print("You ran out of guesses! The answer was: " + number)
