#Problem
''' A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 x 99.

Find the largest palindrome made from the product of two 3-digit numbers. '''

#Answer
''' 906609 '''

#Code Written & Designed by Kenneth Friedman

#returns true if number is a palindrome
def isPalindrome(n):
	r = 0
	p = n
	while p>0:
		r = 10*r + p%10
		p = p/10
	return r == n

#tracks largest number found
largest = 0
#brute force all possible palindrome values from 101 to 999
for i in xrange(999,100,-1):
	for j in xrange(999,100,-1):
		current = i*j
		if ( isPalindrome(current) and current>largest ):
			largest = current

#prints result
print largest