class Project6:
	def find(self):
		running_total_sqs = 0
		running_total_nums = 0
		for x in range(1, 101):
			running_total_nums += x
			running_total_sqs += (x*x)
		print (str(running_total_nums) + " " + str(running_total_sqs))
		print (str((running_total_nums*running_total_nums) - running_total_sqs))