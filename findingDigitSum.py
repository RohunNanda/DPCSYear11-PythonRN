def findSum(n):
	s = 0

	while (n>0):
		x = n%10
		s = s+x
		n = n//10

	print (s)
findSum(720)