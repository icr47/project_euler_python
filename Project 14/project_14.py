class Project14:

	def run(self):
		current_max_chain = 0
		current_max_num = 0
		for x in range(1, 1000000):
			print(str(x))
			stored_x = x
			temp_max_chain = 0
			while True:
				temp_max_chain += 1
				if stored_x % 2 == 0: # it's even.
					stored_x = (stored_x/2)
				elif stored_x == 1: # we found it!!!
					if temp_max_chain > current_max_chain:
						current_max_chain = temp_max_chain
						current_max_num = x
					break;
				else:
					stored_x = (stored_x*3) + 1
		print(x)