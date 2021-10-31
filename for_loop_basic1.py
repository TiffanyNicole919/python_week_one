# Basic - Print all integers from 0 to 150.
# for a in range(0,151) :
# print(a)

# Print all the multiples of 5 from 5 to 1,000
# for number in range(5,1001) :
#if number % 5 == 0 :
		#print (number)
#Print integers 1 to 100. If divisible by 5, print "Coding" instead. If divisible by 10, print "Coding Dojo".
#for x in range(5,101):
	#if x % 5 == 0:
		#print("Coding")
#else:
	#x % 10 == 0
	#print("Coding Dojo")

#Add odd integers from 0 to 500,000, and print the final sum.
#max = int(input("please enter the maximum value"))
#odd_Sum = 0

#for number in range(1, max + 1):
	#if(number %  2 == 0):
		#odd_Sum = odd_Sum + number
#print("The sum of odd numbers 0 to {0} = {1}" .format(number,odd_Sum))

#Print positive numbers starting at 2018, counting down by fours.

#for x in range(2018, 0, -4):
	#if x > 0:
		#print(x)

#Set three variables: lowNum, highNum, mult. Starting at lowNum and going through highNum, print only the integers that are a multiple of mult. For example, if lowNum=2, highNum=9, and mult=3, the loop should print 3, 6, 9 (on successive lines)

lowNum = 2
highNum = 9
mult = 3

for x in range(lowNum, highNum + 1):
	if x % mult == 0:
		print(x)