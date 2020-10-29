
x = int(input("Enter first integer: "))
y = int(input("Enter second integer: "))
while True:
    operation = input("(a)dd (s)ubtract (m)ultiply (d)ivide?")
    if operation not in ('a', 's', 'm', 'd'):
        # should reject (unless a, s, m or d) and reprompt.
        print("Sorry, not a valid choice")
    else: # if input is a, s, m or d, break out of loop
        break

if operation == "a":
    print("The result is: %d" % (x + y))
elif operation == "s":
    print("The result is: %d" % (x - y))
elif operation == "m":
    print("The result is: %d" % (x * y))
elif operation == "d":
    print("The result is: %f" % (x / y))
