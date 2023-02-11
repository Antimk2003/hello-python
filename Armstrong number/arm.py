A = int(input("enter a number: "))
Z = A
S = 0
while A != 0:
    X = A % 10
    S = S+X*X*X
    A = A//10
if Z == S:
    print("number is Armstrong: ")
else:
    print("number is not Armstrong: ")    
