'''user class that has 2 attribute and 2 meathod and some user
   specific attributes '''
   
class User:
	def __init__(ss, f_n, l_n):
		ss.first_name     = f_n
		ss.last_name      = l_n
		ss.login_attempt  = 0
	
	def greet_user(ss):
		print("hello, " + ss.first_name.title()+" "+ss.last_name )
	
	def describe_user(ss):
		print("name\t" + ss.first_name + " " + ss.last_name)
	
	def login_attempts(ss):
		ss.login_attempt += 1
	
	def reset_login_attempts(ss):
		ss.login_attempt = 0
#now making instances.

u1 = User("aa", "bb" )
u2 = User("and", "vro")
u3 = User("rosy", "hage")

'''u1.describe_user()
u2.describe_user()
u3.describe_user()
u1.greet_user()'''

#9.5

u4 = User("beginer", "user")

for i in range(500):
	u4.login_attempts()

print(u4.login_attempt)
print("\v")
u4.reset_login_attempts()
print(u4.login_attempt)
