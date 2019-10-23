import time 
import os

framelist = [
'''
   +---+
   O   |
  /|\  |
  / \  |
      === ''' , '''
   +---+ 
  \O/  |
   |   |
   \\\\  |
      ===''' 
]

while True:
	for frame in framelist:
		os.system("cls")
		print(frame)
		time.sleep(.2)