''' inner class '''

class Lang:
	
	def __init__(self,lan1,lan2,lan3):
		
		self.lan1 = lan1
		self.lan2 = lan2
		self.lan3 = lan3
		self.hindi = self.Hindi()       
        #we have to make an attribute that connect/calls with inner class.		   
	
	def list_lan(self):
		print(self.lan1, self.lan2, self.lan3)


	class Hindi:
		
		def word(self, w1, w2, w3):
			self.word1 = w1
			self.word2 = w2
			self.word3 = w3
		
		def print_word(self):
			print(self.word1, self.word2, self.word3)	
			

l = Lang("spanish", "math", "english")
l.list_lan()
l.hindi.word("a","b","c")
l.hindi.print_word()

