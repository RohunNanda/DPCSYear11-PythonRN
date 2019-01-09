def findGCF (num, den):
	if num > den:
		low = den
	else:
		low = num
	for i in range(1, low+1):
		if((num%i == 0) and (den%i==0)):
			gcf = i
	return gcf

num1 = 6
den1 = 18


print("The GCF of", num1, "and", den1, "is", findGCF(num1, den1))

