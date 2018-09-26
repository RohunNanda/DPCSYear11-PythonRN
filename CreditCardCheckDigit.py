

def cardSum(n):
	s = 0
	ctr = 0
	while (n > 0):
		#print(ctr%2)
		if ctr%2 == 0:
			s = s + n%10
		else:
			x = n%10 * 2 
			while (x > 0):
				s = s + x%10
				x = x//10 
		ctr = ctr + 1
		#print(n%10)
		#s = s + n%10
		n = n //10

	return(s)





card = 7876326826

val = cardSum(card)

if val%10 == 0:
	print ("VALID")
else:
	print ("INVALID")



