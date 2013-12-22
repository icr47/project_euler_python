class LargestPrimeFactor():
	def FindIt(self, num):
		numbers_to_search = list()
		numbers_pos = list()
		p = 3
		while True: 
			if p < num:
				if num % p == 0 and num != p: #throw out that number...
					numbers_pos.append(p)
				p = p + 1
			else:
				break
		print(numbers_pos)
	def FindFactors(self, max):
		current_num = 0 #init out value.
		max_num = (max / 2)
		factors = list() #let's make sure the we don't forget this..
		factors.append(max)
		factors.remove(1)
		if float(max_num).is_integer() == True:
			factors.append(max_num)
			factors.append(2)
		else:
			max_num = round(max_num,0)
			if max % 2 == 0 and max_num % 2 == 0: #both even...
				pass
			else:
				max_num = max_num - 1 # round down by 1.
		#Let's see if it's even or odd! 
		if float((max_num / 2)).is_integer() == True:
			# It's divisible by 2 - let's find all of the factors!
			current_num = max_num / 2 #Seed value.
			factors.append(2)
			factors.append(max_num)
			while float((current_num)).is_integer() == True and (current_num / 2) != 0:
				current_num = current_num / 2
				print(current_num)
				factors.append(2)
				factors.append(current_num)
				
		print (factors)
	def CheckIfPrime (num):
		pass
	
	