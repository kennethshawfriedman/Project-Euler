#Problem
''' By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number? '''

#Answer
''' 104743 '''

#Code Written & Designed by Kenneth Friedman

primeToFind = 10001

#returns True if number is prime
def isPrime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True

currentNumber = 0
primesFound = 0

#loop until found the desired prime
while (primesFound <= primeToFind):
	currentNumber += 1
	#if prime, increment number found
	if isPrime(currentNumber):
		primesFound+= 1

#prints the primeToFind-th prime
print currentNumber