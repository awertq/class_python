'''user class that has 2 attribute and 2 meathod and some user
   specific attributes '''
   
class User:
	def __init__(ss, f_n, l_n):
		ss.first_name = f_n
		ss.last_name  = l_n
	def greet_user(ss):
		print("hello, " + ss.first_name.title()+" "+ss.last_name )
	
	def describe_user(ss):
		print("name\t" + ss.first_name + " " + ss.last_name)

#now making instances.

u1 = User("aa", "bb" )
u2 = User("and", "vro")
u3 = User("rosy", "rozana")

u1.describe_user()
u2.describe_user()
u3.describe_user()
u1.greet_user()


#9.8

class Admin(User):
	def __init__(self):
		self.privileges = Privileges()


class Privileges:
	
	def __init__(self):
		self.privilege = ("can add","can remove","can assign privileges")
	
	def show_privileges(self):
		print(self.privilege)


admin_1 = Admin()
admin_1.privileges.show_privileges()

















