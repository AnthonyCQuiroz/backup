print ("Welcome to the To Do List!")
todolist = []
while True:
	print("Enter a to add an item")
	print("Enter r to remove an item")
	print("Enter p to print the list")
	print("Enter q to quit")
	choice = input("Make your choice: ")

	if choice == "q":
		break
	elif choice == "a":
		# add an item to the list 
		add = input("What would you like to add to the list? ")
		todolist.append(add)
		
		
	elif choice == "r":
		# remove an item from the list 
		remove = input("What would you like to remove? ")
		todolist.remove(remove)
	
	elif choice == "p":
		# print the list 
		print(todolist)
	else: 
		print("This was not a choice, try again")

