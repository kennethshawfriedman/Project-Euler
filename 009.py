#Problem
''' A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 32 + 42 = 9 + 16 = 25 = 52.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc. '''

#Answer
''' 31875000 '''

#Code Written & Designed by Kenneth Friedman

def getKFrom(a,b):
	return (a**2 + b**2)**0.5

#loop for iA
for i in xrange(0, 1000):
	#loop for j
	for j in xrange(i, 1000):
		#get k
		k = getKFrom(i,j)
		#test for accuracy
		if (i+j+k == 1000):
			product = i*j*k
			print int(product)