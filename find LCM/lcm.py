n1 = int(input("enter the first number: "))
n2 = int(input("enter the second number: "))

if n1 > n2:
    digit = n1
else:
    digit = n2
while(True):
    if(digit%n1 == 0 and digit%n2 == 0):
        lcm = digit
        break 
    digit += 1
print("the LCM is :",lcm)       
