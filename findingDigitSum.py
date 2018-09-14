def findSum(n):
	s = 0

	while (n>0):
		x = n%10
		s = s+x
		n = n//10

	return(s)
findSum(720)

def checkHarshad(n):

	if(n%findSum(n)==0):
		return True

	return False 

print(checkHarshad(720));

low = 80
high = 100

for i in range(low,high,1):

	print(checkHarshad(i));