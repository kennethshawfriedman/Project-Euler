#Problem
''' The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million. '''

#Solution
''' 142913828922 '''

#Code Written & Designed by Kenneth Friedman

#returns True if number is prime
def isPrime(n):
	if n == 2 or n==3:
		return True
	if n % 2 == 0:
		return False
	if n % 3 == 0:
		return False
 
	i = 5
	w = 2
	while i * i <= n:
		if n % i == 0:
			return False
		i += w
		w = 6 - w
	return True

sum = 0
top = 2000000

for i in xrange(2,top):
	if isPrime(i):
		sum += i

print sum