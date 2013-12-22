class Prob5:
	def find(self):
		i = 0
		checklist = [11,13,14,16,17,18,19,20]
		while True:
			i+=20
			if all(i % x == 0 for x in checklist):
				# continue loop
				print("heoh we found it! " + str(i))