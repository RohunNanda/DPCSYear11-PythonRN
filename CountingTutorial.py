def misp1LoopStringNumberForward(n):
	print("Somethign")
	for i in range(0, len(n), 1): #Start i at 0 and increment by 1 each time. i < len(n)
		print(n[i])
		x = int(n[i]) #casting to int



def misp1LoopStringNumberBackwards(n):
	print("Somethign")
	for i in range(len(n) - 1, -1 , -1): #Starts at last index, decrement by 1 each time, i > -1
		print(n[i])



def misp2LoopInteger(n):
	#If you are dealing with a numeric type a while loop is the way to go
	while (n > 0):
		print(n%10)
		n = n //10

misp1LoopStringNumberForward("123456789")
print("********")
misp1LoopStringNumberBackwards("123456789")
print("********")
misp2LoopInteger(123456789)