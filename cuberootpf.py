# This program finds the cube root of a perfect integer cube if one enters such a number

num = int(raw_input("Enter a number: "))
ans = 0
while ans*ans*ans < abs(num):
  ans = ans + 1
if ans*ans*ans != abs(num):
  print num, "is not a perfect cube"
else:
  if num < 0:
    ans = -ans
  print "Cube root of ", num, "is ", ans
