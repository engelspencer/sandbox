password = "no memes"
while(password != "memes"):
	password = input("Enter your password\n>")
	print(password)
	if(password == "memes"):
		print("You are now logged in.")
	else:
		print("Access denied. Please try again.")
