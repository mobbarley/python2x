# Testing for boolean expression using an array or a list
list = ["Life","The Universe","Everything","Jack","Jill","Life","Jill"]
#Copying the list
copy = list[:]
#sorting the copied list
copy.sort()
prev = copy[0]
del copy[0]
count = 0

#Go through the list while searching for a match
while(count < len(copy) and copy[count] != prev):
	prev = copy[count]
	count = count + 1
#If a match was not found then count can't be < len
#since the while loop continues while count is < len
#and not match is found
if count < len(copy):
	print("First Match: ",prev)

