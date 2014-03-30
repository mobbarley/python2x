# This program mocks the script for the game fizz - buzz where we print all the numbers
# from 1 to the number entered by the user but we say Fizz when number is divisible by 3 
# and Buzz when it is divisible by 5, when it is both like in 15, 30 etc we will say FizzBuzz

num = int(raw_input("Enter a number : "))
if num < 0:
   print "Invalid number ", num
else:
   for ix in range(1,num+1):
     text = ''
     if ix%3 == 0:
       text = text + "Fizz"
     if ix%5 == 0:
       text = text + "Buzz"
     if text == '':
	print ix
     else:
	print text


	