# Name: Anthony Quiroz
# Period 6
# Dice Rolling Simulator

import random 

#Ask user to input number times of a 6 sided die should be rolled
rolls = int(input("How many rolls would you like to roll? "))

print("Total Rolls: " + str(rolls))

# Create a loop that will run the number of times inputed
x =1

a = 0
b = 0
c = 0
d = 0
e = 0
f = 0

while x <= rolls:
	number = random.randint(1,6)
	if number == 1:
		a += 1
	if number == 2:
		b += 1
	if number == 3:
		c += 1
	if number == 4:
		d += 1
	if number == 5:
		e += 1
	if number == 6:
		f += 1
	print("roll " + str(x) + " is " + str(number))
	x = x+1

print("\n")

print("1s - " + str(a))
print("2s - " + str(b))
print("3s - " + str(c))
print("4s - " + str(d))
print("5s - " + str(e))
print("6s - " + str(f))

print("\n")


print("1s - "  + str((a/rolls)* 100) + "%")
print("2s - "  + str((b/rolls)* 100) + "%")
print("3s - "  + str((c/rolls)* 100) + "%")
print("4s - "  + str((d/rolls)* 100) + "%")
print("5s - "  + str((e/rolls)* 100) + "%")
print("6s - "  + str((f/rolls)* 100) + "%")

