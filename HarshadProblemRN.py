
#The objective of this programme is see how many consecutive Harshad numbers are in a range from "low" to "high"

#Function, findSum, finds the sum of the digits of a number to check that it is a Harshad number
def findSum(n):
	s = 0

	while (n>0): #n is greater than 0 since 0 is a Harshad number itself
		x = n%10 #x = n modulus 10
		s = s+x #s = s + n modulus 10
		n = n//10 #n = n floor division 10

	return(s)
findSum(720) #function findSum verifies that 720 is a Harshad number

def checkHarshad(n): #Function "checkHarshad" is used to check is if a specific number is a Harshad number; if it is a Harshad number "True" will be printed, else "False will be printed"

	if(n%findSum(n)==0):
		return True


	return False 

print(checkHarshad(720));

low = 21 #Low represents the minimum number in the range to finding the Harshad number
high = 69 #High represents the maximum in the range to finding the Harshad number

score = 0 #score is the starting count; for each consecutive Harshad number, "1" is added to indicate the amuont of consecutive Harshad numbers
highScore = 0 #highScore is the count for how many consecutive Harshad numbers in a range from "low" to "high"
#
for i in range(low,high + 1,1): #i = interger; range is from high to low
	if (checkHarshad(i)): #if the number is Harshad number, the consecutive number count, or the score, is +1
		score = score +1; #indicates 
	else:
		highScore = max(score,highScore)
		score = 0; #resets the count for consecutive Harshad numbers

highScore = max(score,highScore)
print(highScore)

#f = open("DwiteHarshadNumbersData.txt", "r")
	
#for line in f:
	#l = f.readline()
	#h = f.readline()
	#checkHarshad (l,h) 

#f.close()

#Commented lines disrupted programme (40-47)