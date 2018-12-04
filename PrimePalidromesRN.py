#preconditions:
#	- number must be n>=2 and n<=999,999
#	- number must a prime number 
#	- number must be a palindrome
#if this is true, then check how many prime palindrome numbers are present between a given range

#Step3: Check if the number is a prime palindrome...
#def checkPrimePalindrome():
	#sampleNum = 181
	#resultP = checkPrime(sampleNum)
	#Do something with result. 
	#if resultP == True:
		#resultPP = checkPalindrome(sampleNum)
		#if resultPP == True:
			#return True
			#return #You can do a straight return with no value.  It ends the method
	
	#return False #catch all value
#This function is unnecessary since it is a test case and only checks if a certain number is both prime and a palindrome

#Step1: Check if the number is prime 
def checkPrime(num):
	if num<2:
		return False
	for i in range(2, num//2+1, 1):	
		if num%i == 0:
			return False
	return True

#Step2: Check if the number is a palindrome
'''def checkPalindrome(num):
	if len(num)==1:
		return True
	if len(num)==2 and num[0] == num[1]:
		return True
	if len(num)==3 and num[0] == num[2]:
		return True
	if len(num)==4 and num[0] == num[3] and num[1] == num[2]:
		return True
	if len(num)==5 and num[0] == num[4] and num[1] == num[3]:
		return True
	if len(num)==6 and num[0] == num[5] and num[1] == num[4] and num[2] == num[3]:
		return True
	return False
The notation needs to be consistent therefore, the "checkPalindrome" needs to be in the integer notation
'''


#Step2: Check if the number is a palindrome 
def checkPalindrome(n):
	num = n
	d = 0
	r = 0
	while n > 0:
		d = n%10
		n = int(n/10) #Creates "n" into integer notation, not a string notation.
		r = r*10 + d

	if (num == r):
		return True
	else:	
		return False

#Step4: Create a loop checking the amount of PrimePalindrome between a range greater than 2 and less than 999,999
def checkLoopPrimePalindrome(low, high):
	ctr = 0

	for i in range(high, low - 1, -1):
		if checkPrime(n) == True and checkPalindrome(n) == True:
			ctr = ctr + 1
	return ctr
#This type of notation is only applicable to strings
#This algorithm is very inefficient but takes advantage of the fact that the maximum length of a number is six digits long or n<999,999


#Tester Code
#Test Prime
#checkPrimePalindrome()
#print("Test check Prime",checkPrime(181)) #returns "True" and seven is a prime number

#Test checkPalindrome    
#print("Test check Palndrome:",checkPalindrome(181)) #returns "True" and 10001 is a prime number

#Test checkPrimePalindrom 
#print("Test check PrimePalindrome",checkPrimePalindrome())

#The "Prime Palindromes" prompt requires that requires that the sample input includes three sets of data only:
print("The amount of Prime Palindromes within the range is", checkLoopPrimePalindrome(2, 100))
print("The amount of Prime Palindromes within the range is", checkLoopPrimePalindrome(100, 200))
print("The amount of Prime Palindromes within the range is", checkLoopPrimePalindrome(200, 1000))
