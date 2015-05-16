#Problem
''' The sum of the squares of the first ten natural numbers is,

12 + 22 + ... + 102 = 385
The square of the sum of the first ten natural numbers is,

(1 + 2 + ... + 10)2 = 552 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum. '''

#Answer
''' 25164150 '''

#Code Written & Designed by Kenneth Friedman

#how many numbers to process
amount = 100

#sumOfSquares
sumOfSquares = 0
for i in xrange(0,amount):
	sumOfSquares += i**2

#squareOfSums
sumOfReg = 0
for i in xrange(0,amount):
	sumOfReg += i
squareOfSums = sumOfReg**2

#computes difference
result = squareOfSums - sumOfSquares

#prints answer
print result

