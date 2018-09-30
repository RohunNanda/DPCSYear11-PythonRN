#Algorithm to solve to see whether a credit card is valid
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





card = 476456874 #Input any credit card number to be analyzed

val = cardSum(card) #val = function to analyze validity of credit card number

if val%10 == 0: #if statement: if the final calculated value of cardSum divided by ten equals zero, then the program shold print "VALID"
#val%10 == 0: value should be perfectly visible by 10; this is indicated through the "== 0"
	print ("VALID")
else: #else statement: otherwise if cardSum is not perfectly divisible by ten, then the program should print "INVALID"
	print ("INVALID")



