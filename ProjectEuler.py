class pe:
	def problem1(self, below, *mults): # Solved
		runningTotal = 0
		i = 0
		while i < below:
			totMult = 1
			for mult in mults:
				totMult = totMult * mult
				if i % mult == 0:
					runningTotal += i
			if i % totMult == 0:
				runningTotal -= i
			i += 1;
		print(runningTotal)
	#prob 2
	def get_next_fib(self):
		prevNum2 = 2
		prevNum = 1
		runningTotal = 2
		cur_fib = 2
		while cur_fib < 4000000:
			cur_fib = prevNum + prevNum2
			prevNum = prevNum2
			prevNum2 = cur_fib
			if cur_fib < 4000000:
				if cur_fib % 2 == 0:
					runningTotal += cur_fib
			else:
				print('fin.\n')
				print (runningTotal)
	#prob 3	
	def get_prime(self, max):
		i = max
		facts = []
		while i > 0:
			if i % 2 == 0 and i != 2: # it's even, so not prime. throw away!
				pass;
			elif max % 5 == 0 and i != 5 # it's a x5, not prime. Throw away.
			elif max % i == 0:
				facts.append(i)
			i -= 1
		print(facts)
		return facts
		
	#def get_prime(self, factors):
	#	primes = []
	#	for fact in factors:
	#		matches = 0
	#		i = fact
	#		while i > 0:
	#			if fact % i == 0:
	#				matches += 1
	#			i -= 1
	#		if matches == 2:
	#			primes.append(fact)
	#	print(primes)
	
	def get_max_prime(self, max):
	#	facts = self.get_fact_noneven(max)
		self.get_prime(max)
				
		
