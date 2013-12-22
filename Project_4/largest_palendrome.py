class LargestPalendrome():

	def FindIt(self):
		cur_large = 0
		for i1 in range(999, 100, -1):
			for i2 in range(999, 100, -1):
				num = i1 * i2
				if str(num) == (str(num)[::-1]): # num -> str -> reverse -> num
					if cur_large < num:
						cur_large = num
		print cur_large