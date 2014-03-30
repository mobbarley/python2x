# This program mocks the abs() function
# allthough this is a standalone and cannot be called

n = int(raw_input("Input an integer:"))
if n < 0 :
    print("The absolute value of ",n," is ",-n)
else:
    print("The absolute value of ",n," is ",n)

