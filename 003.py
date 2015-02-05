#Problem
''' The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ? '''

#Answer
''' 6857 '''

#Code Written & Designed by Kenneth Friedman

#start with full number and reduce
largestPrime = 600851475143
#tracking number
i = 2

#loop until largestPrime is greater than tracking number
while i**2 < largestPrime:
     #divide by tracker until no longer evenly divisible
     while largestPrime % i == 0:
         largestPrime = largestPrime / i
     i = i + 1

#prints solution
print largestPrime