#Problem
''' 2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20? '''

#Answer
''' 232792560 '''

#Code Written & Designed by Kenneth Friedman

low = 1
high = 20

result = 1

#main loop
for i in (range(low, high+1)):
    #if not divisible yet
    if result % i > 0:
    	#find needed components (in inner loop)
        for j in range(1, 21):
            if (result*j) % i == 0:
                result *= j
                break

#prints answer
print result