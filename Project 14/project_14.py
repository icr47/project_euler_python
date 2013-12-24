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
		#WARNING: REALLY SLOW
	def run_faster(self):
		current_max_chain = 0
		list_of_numbers = []
		for x in range(1000001,1, -1):
			print(x)
			stored_x = x
			temp_max_chain = 0
			current_chain_list = []
			while True:
				if stored_x in list_of_numbers:
					#print("one was in the chain ;)")
					# first, find the length of the chain.
					i = list_of_numbers.index(stored_x)
					current_max_chain += (len(list_of_numbers) - i)
					# next, insert the chain 
					if i == 0:
						for y in range(0, (len(current_chain_list)-1)):
							list_of_numbers.insert(y,current_chain_list[y])
						break
				temp_max_chain += 1
				if stored_x % 2 == 0: # it's even.
					stored_x = (stored_x/2)
					current_chain_list.append(stored_x)
				elif stored_x == 1: # we found it!!!
					for y in range(0, (len(current_chain_list)-1)):
						list_of_numbers.insert(y,current_chain_list[y])
					if temp_max_chain > current_max_chain:
						current_max_chain = temp_max_chain
					break;
				else:
					stored_x = (stored_x*3) + 1
					current_chain_list.append(stored_x)
		print(current_max_chain)