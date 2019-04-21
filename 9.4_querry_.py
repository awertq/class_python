''' making a class restaurant having 2 attribute name and cusine type 
    and 2 methods '''

class Restaurant:
    def __init__(self, restaurant_name, cusine_type, n_s=0):
        self.restaurant_name = restaurant_name
        self.cusine_type     = cusine_type
        self.number_served  = n_s

    def describe_restaurant(self):
		print("restuarant name is " + self.restaurant_name.title())
		print("cusine offered is " + self.cusine_type.title())
		if self.number_served >0:
			print(self.number_served)
    
    def open_restaurant(self):
		print("the restaurant is open now.")
	
    def increment_n_s(self, i_n_s):
		self.number_served += i_n_s 
		return self.number_served
	
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
r3.describe_restaurant()'''

#9.4

resto = Restaurant("restaurant", "indian,thai,italian", 592)
print(resto.describe_restaurant())
                                   #querry -> during running i get none in end? why??

print("new number of cusomer served is ",resto.increment_n_s(8))
                          '''here first it show none but after using return keyword if 
                             shows the number !'''
