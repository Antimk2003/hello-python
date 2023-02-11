x = int(input("enter a number: "))
first = 0
second = 1
for i in range(1,x):
    print(first)
    third = first +second
    first = second
    second = third
