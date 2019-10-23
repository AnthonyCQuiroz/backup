import time 
import os

framelist = [
'''
         




                    __________________________
                   /                         \\
                  /                           \\
                 /                             \\
                |    __________   __________    |
                |                               |                 
                |                |              |
                |                |              |
                |                |}             |
                |                               |
                |                   __          |
                |                  |  |         |
                |                  \\__\\       |
                \\
                 \\
                  \\


''' ,
'''









                     <>   <> 
                        |  
                      \\___/   ''' ,
'''










                     __
                    |[]|
                    |  |
               _____|  |_____
              |  |  |  |  |  |
              |  |        |  |____
              |              _____|
              \\           _/
               \\         /
                \\       /    '''
]

while True:
	for frame in framelist:
		os.system("cls")
		print(frame)
		time.sleep(.6)