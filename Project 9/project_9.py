import time

class Project9:
	def find(self):
		start_time = time.clock() # using timer for benchmarking.
		a = 0
		b = 1
		c = 1000
		for a in range(0, 499): # since it a < b, where a = int, we know that a = (b-1).
			for b in range(1, 500): # since b < c where b = int, we know that b = (c/2) since c cannot equal or be greater than b 
				c = (1000 - a) - b # set c to the correct value everytime. Probably a more efficient method, but this works.
				if a < b and b < c:
						if ((a + b) + c) == 1000:
							if self.check_sqr(a, b, c) == True: 
								print("It took " + str(time.clock() - start_time))
								return
	def check_sqr(self, a, b, c): #checks if it's a valid solution. 
		if (pow(a, 2) + pow(b, 2)) == (pow(c, 2)): # YES! WE FOUND IT!!!
			print("We found it. Here's the numbers:")
			print("\n" + str(a))
			print("\n" + str(b))
			print("\n" + str(c))
			print('\n a*b*c = ' + str((a*b)*c))
			return True
		else:
			return False