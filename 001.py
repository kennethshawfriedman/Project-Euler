#Problem
''' If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000. '''

#Answer
'''233168'''

#Code Written & Designed by Kenneth Friedman

#return True if i is a multiple of 3 or 5
def isMultiple(i):
	return (i % 3 == 0 or i % 5 == 0)

#sum of all the numbers
sum = 0

#loop to check all numbers less than 1,000
for i in xrange(0,1000):
	if (isMultiple(i)):
		sum+= i

#prints answer
print sum