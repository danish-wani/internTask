import sys

number=int(sys.argv[1])

#factorial function

def factorial(number):
	if(number==1):
		return 1
	return(factorial(number-1)*number)

fact=factorial(number)
print(fact)
