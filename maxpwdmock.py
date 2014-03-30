#This program mocks up the test for a the number of times a password is entered
# and denies access if the count exceeds a certain value

max_count = 5
passwd = "elsa"
instr = str(raw_input("Enter the password ! : "))
count = 1
while(instr != passwd and count < max_count):
    count = count + 1
    print("Wrong password!..Try again")
    instr = str(raw_input("Enter the password ! : "))
if count < max_count:
    print("Password Ok. Access granted")
else:
    print("Maximum counts exceeded. Access denied")
    
