#9.14

import random as r

ran_int = r.randint(1,6)

class Die:
	def __init__(self,sides=6):
		self.sides = sides
		
	def roll_die(self):
		print(r.randint(1,self.sides))
		

die_6 = Die(6)
for roll in range(10):
	die_6.roll_die()
print("\v")	
die_10 = Die(10)
for i in range(10):
	die_10.roll_die()
	
