first = input("What is the first number? ")
second = input("What is the second number? ")

if first > second:
    print("The first number is greater")
elif first <= second:
    print("The first number is not greater")

if first == second:
    print("The numbers are equal")

if second > first:
    print("The second number is greater")
elif second <= first:
    print("The second number is not greater")

my_fave = "elephant"
their_fave = input("\nWhat is your favorite animal? ").lower()

if my_fave == their_fave:
    print("That's my favorite animal too!")
elif my_fave == my_fave:
    print("That one is not my favorite.")



'''
Alternate solution for the first one:
first = input("What is the first number? ")
second = input("What is the second number? ")
print("The first number is " + ("" if first > second else "not ") + "greater")
print("The numbers are " + ("" if first == second else "not ") + "equal")
print("The second number is " + ("" if second > first else "not ") + "greater")

'''