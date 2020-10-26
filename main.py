x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))

while True:
    operation = input("(a)dd (s)ubtract (m)ultiply (d)ivide?")
    if operation.islower() not in ('a', 's', 'm', 'd'):
        print("Sorry, not a valid choice")
    else:
        break

if operation == "a":
    print("The result is: %d" % (x + y))
elif operation == "s":
    print("The result is: %d" % (x - y))
elif operation == "m":
    print("The result is: %d" % (x * y))
elif operation == "d":
    print("The result is: %d" % (x / y))
