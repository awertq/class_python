'''do i have to specify the attribute while setting it defalt '''
'''class Car:
    def __init__(self, year, name):
        self.year = year
        self.name = name
        self.distance = 0
c1 = Car(1996, "maruti800")
c2 = Car(2019, "wagonr")
print("\v")
print(c1.year," ", c1.name)          #printing initial detailes
print("\v")
c1.distance = 6000
print(c1.distance)
'''

#super() experimentation

class Sup:

	def __init__(self,com1,com2,com3):
		self.c1 =com1
		self.c2 =com2
		self.c3 =com3

	def list_coms(self):
		print(self.c1, self.c2, self.c3)



class Sub(Sup):

	def __init__(self):
		print("this is child class baby")

		super().__init__('com1','com2',"com3")
		super().list_coms()

c_l = Sub()
