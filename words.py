students=[]
cont="1"
while cont=="1":
	students.append(input("Add a student: "))
	print(students)
	cont=input("Do you want to add another student? (0 is no, 1 is yes)")
	if cont != "0" and cont != "1":
		cont="0"

