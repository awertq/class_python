''' making a class restaurant having 2 attribute name and cusine type 
    and 2 methods '''

class Restaurant:
    def __init__(self, restaurant_name, cusine_type):
        self.restaurant_name = restaurant_name
        self.cusine_type     = cusine_type

    def describe_restaurant(self):
        print("restuarant name is " + self.restaurant_name.title())
        print("cusine offered is " + self.cusine_type.title())

    def open_restaurant(self):
        print("the restaurant is open now.")


''' making instance with Restaurant class '''

''' restaurant = Restaurant("punjabi dhaba", "traditional punjabi cusine")

print("restaurant name is "+restaurant.restaurant_name.title())
print("restaurant cusine offered is "+restaurant.cusine_type.title())
print()
print("calling first describing meathod \t")
restaurant.describe_restaurant()
print()
print("callind seacond open sign indicating meathod \t")
restaurant.open_restaurant()
'''

'''r1 = Restaurant("indian restaurant", "indian")
r2 = Restaurant("chinese restaurant", "chinese")
r3 = Restaurant("thai reataurant", "thai")

print("calling describing meathod ")
print()
r1.describe_restaurant()
print()
r2.describe_restaurant()
print()
r3.describe_restaurant()
'''

#9.6
class Ice_cream_stand(Restaurant):
	
	def __init__(self, s_n):
		self.stand_name = s_n
		self.flavor     = Flavor()
		


class Flavor:
	def __init__(self):
		self.flavors = ("banana","blueberry","raspberry","strawberry","lotus")
		
	def list_flavors(self):
		print(self.flavors)


krishna_IC = Ice_cream_stand("Krishna_IC")
krishna_IC.flavor.list_flavors()
		
			






