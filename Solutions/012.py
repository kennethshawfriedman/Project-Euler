#Problem
''' The sequence of triangle numbers is generated by adding the natural numbers. So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. The first ten terms would be:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors? '''

#Answer
'''  '''

#Code Written & Designed by Kenneth Friedman

#returns number of divisors of the input
def numberOfDivisors(n):
	num = 1
	while n % 2 == 0:
		num += 1
		n = n/2
	for x in xrange(1, n/2+1):
		if (n % x == 0):
			num += 1
	print num
	return num

#tries to get number of divisors starting at 1, increasing by 1 until numDivisors is about count
def testNumsUntil(count):
	first = 0
	current = 100000
	while current<200000:
		current += 1
		if (numberOfDivisors(current)>count):
			return current

numberOfDivisors(28)

#prints result
#result = testNumsUntil(500)
#print result
